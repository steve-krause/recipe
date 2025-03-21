import './App.css'
import Navbar from './components/Navbar';
import Information from './components/Information';
import Ingredients from './components/Ingredients';
import Instructions from './components/Instructions';

function App() {

  return (
    <>
      <title>Apple Banana Quinoa Breakfast Cups</title>
      <Navbar />
      <Information />
      <Ingredients />
      <Instructions />
    </>
  );
}

export default App
