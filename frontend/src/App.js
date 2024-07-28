import "./App.css";
import Home from "./components/Home/Home";
import TopNavbar from "./components/TopNavbar/TopNavbar";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <TopNavbar />
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </div>
  );
}

export default App;
