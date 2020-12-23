import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import {useEffect, useState} from "react";
import { BASE_URL_DEV } from './config'

const App = () => {

  const [users, setUsers] = useState([]);

  useEffect(() => {
      if ( users.length === 0 ) {
          axios.get(BASE_URL_DEV+`api/v1/users/list`)
              .then(res => {
                  const users = res.data.users;
                  console.log(users);
                  setUsers( users );
              });
      }
  }, [users]);

    return (
        <div className="App">
          <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
              {users.length > 0 ?
                  (
                      <ul>
                      {
                          users.map((user) => (
                              <li key={user.id}>{user.username}</li>
                          ))
                      }
                      </ul>
                  ) : (
                      <h3> No data </h3>
                  )
              }
          </header>
        </div>
    );
}

export default App;
