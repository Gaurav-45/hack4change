import "./App.css";
import Home from "./components/Home/Home";
import TopNavbar from "./components/TopNavbar/TopNavbar";
import { Routes, Route } from "react-router-dom";
import Detect from "../src/components/Detect/Detect";
import YPredictor from "./components/yeildPredictor/YPredictor";

function App() {
  return (
    <div className="App">
      <TopNavbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/disdetector" element={<Detect />} />
        <Route path="/price-predictor" element={<YPredictor />} />
      </Routes>
    </div>
  );
}

export default App;
