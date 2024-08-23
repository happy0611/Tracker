import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './component/Header';
import Home from "./component/Home"
import axios from "axios";
import { useEffect, useState } from 'react';

interface Data {
  img: string;
}

const App: React.FC = () => {
  const [data,setData] = useState<Data | null>(null);

  useEffect(() => {
    axios.get("/")
      .then((response) => setData(response.data))
      .catch((error) => console.error(error));
  },[]);

  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Home img={data?.img ?? '/default/path/to/image.jpg'} />} />
        <Route path="/menu" element={<Menu />} />
        <Route path="/locations" element={<Locations />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </Router>
  );
};

const Menu: React.FC = () => {
  return <h2>Menu Page</h2>;
};

const Locations: React.FC = () => {
  return <h2>Locations Page</h2>;
};

const Contact: React.FC = () => {
  return <h2>Contact Page</h2>;
};

export default App;