import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import {useEffect, useState} from "react";
import { BASE_URL_DEV } from './config'

const App = () => {

  const [tasks, setTasks] = useState([]);

  useEffect(() => {
      if ( tasks.length === 0 ) {
          axios.get(BASE_URL_DEV+`api`)
              .then(res => {
                  console.log(res.data);
                  const tasks = res.data;
                  setTasks( tasks );
              });
      }
  }, [tasks]);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <ul>
            { tasks.map(task => <li>{task.title}</li>) }
        </ul>
      </header>
    </div>
  );
}

export default App;
