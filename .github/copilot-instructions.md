<!-- .github/copilot-instructions.md for LAB-PA-AWS -->
# How to help in this repository

This repository is a small React + TypeScript frontend scaffold (Vite) used as a lab for AWS practice. Use these instructions to write focused, repository-aware code changes.

- **Primary area**: `frontend/` — contains the full app (Vite, React, TypeScript).
- **Other areas**: repository root has a short `README.md` describing the lab.

**Architecture (quick)**

- The app is a single-page React + TypeScript application mounted in `frontend/src/main.tsx` and rendered by `frontend/src/App.tsx`.
- Build & tooling are configured in `frontend/package.json` and `frontend/vite.config.ts`. TypeScript project references (if expanded) live in `tsconfig.*.json` files in `frontend/`.
- Static assets and Vite conventions are used (e.g. `/vite.svg` reference in `App.tsx`, SVG imports under `src/assets/`).

**Developer workflows / commands**

Use PowerShell on Windows (this repo was inspected on Windows). Typical commands:

```
cd frontend
npm install
npm run dev      # starts Vite dev server with HMR
npm run build    # runs `tsc -b && vite build` per package.json
npm run preview  # preview built site
```

Notes:
- `npm run build` runs TypeScript build first (`tsc -b`) then `vite build` — be careful when changing `tsconfig.*` files.
- The project uses `rolldown-vite` aliased as `vite` via `overrides` in `package.json`.

**Patterns & repository-specific conventions**

- Importing assets: absolute `/vite.svg` path and local imports like `./assets/react.svg` are used. Use Vite import semantics (ESM).
- React compiler plugin: `frontend/vite.config.ts` configures `@vitejs/plugin-react` with `babel-plugin-react-compiler`. Avoid changing this unless you understand the performance/compile tradeoffs.
- Linting: ESLint is present (see `frontend/eslint.config.js`) and TypeScript-aware linting is hinted in `frontend/README.md`.

**Files to inspect when making changes**

- `frontend/package.json` — scripts, deps, and devDeps (scripts are authoritative for build/dev flows).
- `frontend/vite.config.ts` — Vite plugins and Babel/react-compiler settings.
- `frontend/src/main.tsx` and `frontend/src/App.tsx` — app entry + root component.
- `frontend/tsconfig.app.json` / `frontend/tsconfig.node.json` — TypeScript project settings referenced by ESLint/Vite when type-aware checks are added.

**What to do (and what to avoid)**

- When fixing frontend bugs: run `npm run dev` locally and reproduce HMR behavior in `App.tsx` or components under `src/`.
- For build issues: run `npm run build` and inspect `tsc` output first, then `vite build` failures.
- Do not change `overrides` or the alias of `vite` without testing builds on both `dev` and `build` scripts — CI or contributors may rely on the current override.

**Examples to reference in changes**

- Example: to add a new page, register a new entry in `frontend/src` and render it from `App.tsx`; ensure assets are imported using Vite paths.
- Example: to change bundling plugins, update `frontend/vite.config.ts` and run `npm run build` locally to validate both `tsc` and `vite` steps.

**Missing / not present**

- There are no tests or server code in this repository snapshot. If adding tests, include commands in `frontend/package.json` and add instructions here.

If anything in this file is unclear or you'd like more detail for a specific change (e.g., adding a backend, CI steps, or test harness), tell me which area you'd like expanded and I will update this file.
