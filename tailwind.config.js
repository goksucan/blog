/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./core/templates/core/*.html'],
  theme: {
    container:{
      center: true,
      padding: '2rem',
    },
    extend: {
      fontFamily: {
        body: ['Lora'],
        header:['Passion One'],
        headertr:['Abril Fatface']
      },
    },
  },
  plugins: [],
}
