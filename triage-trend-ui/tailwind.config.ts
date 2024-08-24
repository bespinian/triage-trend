import { join } from "path";
import type { Config } from "tailwindcss";
import forms from "@tailwindcss/forms";
import typography from "@tailwindcss/typography";
import daisyui from "daisyui";

export default {
  content: ["./src/**/*.{html,js,svelte,ts}"],
  theme: {
    extend: {},
  },
  plugins: [forms, typography, daisyui],
  daisyui: {
    themes: ["light", "dark", "cupcake", "cyberpunk"],
  },
} satisfies Config;
