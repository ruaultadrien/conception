import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Header from './components/Header';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import CurriculumVitae from './components/CurriculumVitae';
import WorkInProgress from './components/WorkInProgress';


function App() {
    return (
        <Router>
            <Header />
            <Routes>
                <Route path="/" element={<CurriculumVitae />} />
                <Route path="/home" element={<CurriculumVitae />} />
                <Route path="/word_machine" element={<WorkInProgress />} />
                <Route path="/climate_machine" element={<WorkInProgress />} />
            </Routes>
        </Router>
    );
}

export default App;
