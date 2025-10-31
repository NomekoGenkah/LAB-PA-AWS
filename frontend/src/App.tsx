import './App.css'
import HomePage from './pages/HomePage'

function App() {

  return (
    <>
    <h1>Transparencia</h1>

    <div className='cards-holder'>
      <div className='card'>
        <h2>Gastos</h2>
        <p>Veja os gastos detalhados do governo.</p>
      </div>

      <div className='card'>
        <h2>Receitas</h2>
        <p>Confira as fontes de receita do governo.</p>
      </div>

      <div className='card'>
        <h2>Contratos</h2>
        <p>Acesse os contratos firmados pelo governo.</p>
      </div>
    </div>
    <HomePage />


    </>
  )
}

export default App
