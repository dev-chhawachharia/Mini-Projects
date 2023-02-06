import Header from './components/Header';
import data from "./data";
import './App.css';
import Main from './components/Main';

function App() {
  const card = data.map(items => {
      return(
        <div className="app-div">
          <Main 
          key={items.id}
          item={items}
          />
        </div>
      )
    })
  return (
    <>
      <Header />
      <main className="main-container">
        {card}
      </main>
    </>
  );
}

export default App;
