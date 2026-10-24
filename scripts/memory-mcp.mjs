import { spawn } from "node:child_process";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const raiz = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const rutaGrafo = join(raiz, "docs", "memoria", "memoria.local.json");
const entorno = { ...process.env, MEMORY_FILE_PATH: rutaGrafo };
const comando = process.platform === "win32" ? "npx.cmd" : "npx";

const servidor = spawn(
  comando,
  ["-y", "@modelcontextprotocol/server-memory"],
  {
    env: entorno,
    stdio: "inherit",
    shell: process.platform === "win32",
  },
);

servidor.on("error", (error) => {
  console.error(`No se pudo iniciar el Memory MCP: ${error.message}`);
  process.exit(1);
});

servidor.on("exit", (codigo, senal) => {
  process.exit(codigo ?? (senal ? 1 : 0));
});

for (const senal of ["SIGINT", "SIGTERM"]) {
  process.on(senal, () => servidor.kill(senal));
}
