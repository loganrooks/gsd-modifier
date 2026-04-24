#!/usr/bin/env node
/**
 * Runtime-neutral project instruction generator.
 *
 * This wrapper owns the modifier repo's AGENTS.md generation contract. It
 * intentionally avoids the upstream generate-claude-md body because that
 * command still carries CLAUDE.md naming and runtime-specific templates.
 */

const fs = require('fs');
const path = require('path');

const MANAGED_SECTIONS = ['project', 'stack', 'conventions', 'architecture', 'skills', 'workflow'];
const SECTION_HEADINGS = {
  project: '## Project',
  stack: '## Technology Stack',
  conventions: '## Conventions',
  architecture: '## Architecture',
  skills: '## Project Skills',
  workflow: '## GSD Workflow Enforcement',
};
const FALLBACKS = {
  project: 'Project not yet initialized. Run $gsd-new-project to set up.',
  stack: 'Technology stack not yet documented. Will populate after codebase mapping or first phase.',
  conventions: 'Conventions not yet established. Will populate as patterns emerge during development.',
  architecture: 'Architecture not yet mapped. Follow existing patterns found in the codebase.',
  skills: 'No project skills found. Add skills to `.codex/skills/`, `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, or `.github/skills/` with a `SKILL.md` index file.',
};
const WORKFLOW_ENFORCEMENT = [
  'Before using file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.',
  '',
  'Use these entry points:',
  '- `$gsd-quick` for small fixes, doc updates, and ad-hoc tasks',
  '- `$gsd-debug` for investigation and bug fixing',
  '- `$gsd-execute-phase` for planned phase work',
  '',
  'Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.',
].join('\n');
const PROFILE_PLACEHOLDER = [
  '<!-- GSD:profile-start -->',
  '## Developer Profile',
  '',
  '> Profile not yet configured. Run `$gsd-profile-user` to generate your developer profile.',
  '> This section is managed by the GSD profile generator; do not edit manually.',
  '<!-- GSD:profile-end -->',
].join('\n');
const SKILL_SEARCH_DIRS = ['.codex/skills', '.claude/skills', '.agents/skills', '.cursor/skills', '.github/skills'];

function parseArgs(argv) {
  const options = { output: null, runtime: 'unknown' };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === '--output') {
      options.output = argv[i + 1];
      i += 1;
    } else if (arg === '--runtime') {
      options.runtime = argv[i + 1] || 'unknown';
      i += 1;
    } else if (arg === '--help' || arg === '-h') {
      options.help = true;
    }
  }
  return options;
}

function usage() {
  return [
    'Usage: node generate-instruction.cjs --output AGENTS.md [--runtime codex|claude]',
    '',
    'Creates or refreshes GSD marker-bounded sections in a runtime-neutral AGENTS.md file.',
  ].join('\n');
}

function safeRead(filePath) {
  try {
    return fs.existsSync(filePath) ? fs.readFileSync(filePath, 'utf-8') : null;
  } catch {
    return null;
  }
}

function extractMarkdownSection(content, heading) {
  const lines = content.split('\n');
  const headingPattern = new RegExp(`^##\\s+${heading.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\s*$`, 'i');
  const result = [];
  let capturing = false;
  for (const line of lines) {
    if (headingPattern.test(line)) {
      capturing = true;
      result.push(line);
      continue;
    }
    if (capturing && /^##\s+/.test(line)) break;
    if (capturing) result.push(line);
  }
  return result.length > 0 ? result.join('\n').trim() : null;
}

function summarizeStructuredMarkdown(content) {
  const lines = [];
  let inTable = false;
  for (const line of content.split('\n')) {
    if (line.startsWith('#')) {
      if (!line.startsWith('# ') || lines.length > 0) lines.push(line);
      continue;
    }
    if (line.startsWith('|')) {
      inTable = true;
      lines.push(line);
      continue;
    }
    if (inTable && line.trim() === '') inTable = false;
    if (line.startsWith('- ') || line.startsWith('* ') || line.startsWith('```')) lines.push(line);
  }
  return lines.length > 0 ? lines.join('\n') : content.trim();
}

function generateProjectSection(cwd) {
  const content = safeRead(path.join(cwd, '.planning', 'PROJECT.md'));
  if (!content) return { content: FALLBACKS.project, source: 'PROJECT.md', fallback: true };

  const parts = [];
  const h1Match = content.match(/^# (.+)$/m);
  if (h1Match) parts.push(`**${h1Match[1]}**`);

  for (const heading of ['What This Is', 'Core Value', 'Constraints']) {
    const section = extractMarkdownSection(content, heading);
    if (!section) continue;
    const body = section.replace(new RegExp(`^##\\s+${heading}\\s*`, 'i'), '').trim();
    if (!body) continue;
    if (heading === 'Core Value') parts.push(`**Core Value:** ${body}`);
    else if (heading === 'Constraints') parts.push(`### Constraints\n\n${body}`);
    else parts.push(body);
  }

  if (parts.length === 0) return { content: FALLBACKS.project, source: 'PROJECT.md', fallback: true };
  return { content: parts.join('\n\n'), source: 'PROJECT.md', fallback: false };
}

function generateFileBackedSection(cwd, sectionName, candidates) {
  for (const [source, relPath] of candidates) {
    const content = safeRead(path.join(cwd, relPath));
    if (content) return { content: summarizeStructuredMarkdown(content), source, fallback: false };
  }
  return { content: FALLBACKS[sectionName], source: candidates[0][0], fallback: true };
}

function extractSkillFrontmatter(content) {
  const result = { name: '', description: '' };
  const match = content.match(/^---\s*\n([\s\S]*?)\n---/);
  if (!match) return result;

  let currentKey = '';
  for (const line of match[1].split('\n')) {
    const kv = line.match(/^(\w[\w-]*):\s*(.*)/);
    if (kv) {
      currentKey = kv[1];
      if (currentKey === 'name' || currentKey === 'description') {
        result[currentKey] = kv[2].replace(/^["']|["']$/g, '').trim();
      }
      continue;
    }
    if (currentKey === 'description' && /^\s+/.test(line)) {
      result.description += ` ${line.trim()}`;
    }
  }
  return result;
}

function generateSkillsSection(cwd) {
  const discovered = [];
  for (const dir of SKILL_SEARCH_DIRS) {
    const absDir = path.join(cwd, dir);
    if (!fs.existsSync(absDir)) continue;

    let entries;
    try {
      entries = fs.readdirSync(absDir, { withFileTypes: true });
    } catch {
      continue;
    }

    for (const entry of entries) {
      if (!entry.isDirectory() || entry.name.startsWith('gsd-') || entry.name.startsWith('gsdr-')) continue;
      const skillPath = path.join(absDir, entry.name, 'SKILL.md');
      const content = safeRead(skillPath);
      if (!content) continue;
      const frontmatter = extractSkillFrontmatter(content);
      const name = frontmatter.name || entry.name;
      if (discovered.some((skill) => skill.name === name)) continue;
      discovered.push({
        name,
        description: frontmatter.description || '',
        path: `${dir}/${entry.name}`,
      });
    }
  }

  if (discovered.length === 0) return { content: FALLBACKS.skills, source: 'skills/', fallback: true };

  const lines = ['| Skill | Description | Path |', '|-------|-------------|------|'];
  for (const skill of discovered) {
    const name = skill.name.replace(/\|/g, '\\|');
    const description = skill.description.replace(/\|/g, '\\|').replace(/\n/g, ' ').trim();
    lines.push(`| ${name} | ${description} | \`${skill.path}/SKILL.md\` |`);
  }
  return { content: lines.join('\n'), source: 'skills/', fallback: false };
}

function buildSection(sectionName, source, content) {
  return [
    `<!-- GSD:${sectionName}-start source:${source} -->`,
    content,
    `<!-- GSD:${sectionName}-end -->`,
  ].join('\n');
}

function updateSection(fileContent, sectionName, newContent) {
  const startMarker = `<!-- GSD:${sectionName}-start`;
  const endMarker = `<!-- GSD:${sectionName}-end -->`;
  const startIdx = fileContent.indexOf(startMarker);
  const endIdx = fileContent.indexOf(endMarker);
  if (startIdx !== -1 && endIdx !== -1) {
    const before = fileContent.substring(0, startIdx);
    const after = fileContent.substring(endIdx + endMarker.length);
    return before + newContent + after;
  }
  return `${fileContent.trimEnd()}\n\n${newContent}\n`;
}

function generateSections(cwd) {
  return {
    project: generateProjectSection(cwd),
    stack: generateFileBackedSection(cwd, 'stack', [
      ['codebase/STACK.md', '.planning/codebase/STACK.md'],
      ['research/STACK.md', '.planning/research/STACK.md'],
    ]),
    conventions: generateFileBackedSection(cwd, 'conventions', [
      ['CONVENTIONS.md', '.planning/codebase/CONVENTIONS.md'],
    ]),
    architecture: generateFileBackedSection(cwd, 'architecture', [
      ['ARCHITECTURE.md', '.planning/codebase/ARCHITECTURE.md'],
    ]),
    skills: generateSkillsSection(cwd),
    workflow: { content: WORKFLOW_ENFORCEMENT, source: 'GSD defaults', fallback: false },
  };
}

function writeInstructionFile(cwd, outputPath) {
  const generated = generateSections(cwd);
  const sectionsGenerated = [];
  const sectionsFallback = [];
  let action = 'updated';

  let fileContent = safeRead(outputPath);
  if (fileContent === null) {
    action = 'created';
    const parts = [];
    for (const sectionName of MANAGED_SECTIONS) {
      const section = generated[sectionName];
      const body = `${SECTION_HEADINGS[sectionName]}\n\n${section.content}`;
      parts.push(buildSection(sectionName, section.source, body));
      (section.fallback ? sectionsFallback : sectionsGenerated).push(sectionName);
    }
    parts.push('');
    parts.push(PROFILE_PLACEHOLDER);
    fileContent = `${parts.join('\n\n')}\n`;
  } else {
    for (const sectionName of MANAGED_SECTIONS) {
      const section = generated[sectionName];
      const body = `${SECTION_HEADINGS[sectionName]}\n\n${section.content}`;
      fileContent = updateSection(fileContent, sectionName, buildSection(sectionName, section.source, body));
      (section.fallback ? sectionsFallback : sectionsGenerated).push(sectionName);
    }
    if (!fileContent.includes('<!-- GSD:profile-start')) {
      fileContent = `${fileContent.trimEnd()}\n\n${PROFILE_PLACEHOLDER}\n`;
    }
  }

  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, fileContent, 'utf-8');
  return {
    instruction_file_path: outputPath,
    action,
    sections_generated: sectionsGenerated,
    sections_fallback: sectionsFallback,
    sections_total: MANAGED_SECTIONS.length,
    profile_status: fileContent.includes('<!-- GSD:profile-start') ? 'present' : 'absent',
    message: `${action === 'created' ? 'Created' : 'Updated'} AGENTS.md instruction file.`,
  };
}

function main() {
  const options = parseArgs(process.argv.slice(2));
  if (options.help) {
    process.stdout.write(`${usage()}\n`);
    return 0;
  }
  if (!options.output) {
    process.stderr.write(`${usage()}\n`);
    return 2;
  }

  const cwd = process.cwd();
  const outputPath = path.isAbsolute(options.output) ? options.output : path.join(cwd, options.output);
  const result = writeInstructionFile(cwd, outputPath);
  result.runtime = options.runtime;
  process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
  return 0;
}

if (require.main === module) {
  process.exitCode = main();
}

module.exports = {
  writeInstructionFile,
  generateSections,
};
