import "./App.css";
import Home from "./components/Home/Home";
import TopNavbar from "./components/TopNavbar/TopNavbar";
import { Routes, Route } from "react-router-dom";
import Detect from "../src/components/Detect/Detect";

function App() {
  return (
    <div className="App">
      <TopNavbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/disdetector" element={<Detect />} />
      </Routes>
    </div>
  );
}

export default App;
