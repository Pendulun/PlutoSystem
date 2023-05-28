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
      'gray2': '#D9D9D9',
      'gray3': '#666565',
      'gray4': '#898989',
      'gray5' : '#1C1C1C',
      'darkTeal': '#014D4E',
      'lightBlue': '#4CBED7',
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
      'sm14': '14px',
      'bs': '16px',
      'rg': '18px',
      'lg': '22px',
      'xl': '28px',
      '2xl': '36px',
      '3xl': '60px',
    }
  }
}