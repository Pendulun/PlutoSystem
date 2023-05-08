/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    screens: {
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl: '1440px',
    },
    colors: {
      'primary': '#194751',
      'secondary': '#4CBED7',
      'darkGray': '#171717',
      'gray': '#1E1E1E',
      'lightGray': '#2F2F2F',
      'lighterGray': '#666565',
      'white': '#FFFFFF',
    },
    fontFamily: {
      sans: ['Inter', 'sans-serif'],
    },
    fontSize: {
      'xs': '10px',
      'sm': '12px',
      'bs': '16px',
      'rg': '18px',
      'lg': '22px',
      'xl': '28px',
      '2xl': '36px',
      '3xl': '60px',
    }
  }
}
