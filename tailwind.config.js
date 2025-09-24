/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./leohakim_dev/templates/**/*.html",
    "./leohakim_dev/users/**/*.py",
  ],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: "#0ea5e9",
          50: "#f0f9ff",
          100: "#e0f2fe",
          200: "#bae6fd",
          300: "#7dd3fc",
          400: "#38bdf8",
          500: "#0ea5e9",
          600: "#0284c7",
          700: "#0369a1",
          800: "#075985",
          900: "#0c4a6e",
        },
      },
      maxWidth: {
        '8xl': '96rem'
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
};
