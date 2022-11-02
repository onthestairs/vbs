/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,svelte,ts}"],
  theme: {
    extend: {
      width: {
        '128': '32rem',
      },
      fontFamily: {
        "garamond": ["'EB Garamond'", "serif"],
      },
    },
  },
  plugins: [],
};
