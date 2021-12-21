import logo from './logo.svg';
import './App.css';
import {Home} from './Home';
import {Task} from './Task';
import {BrowserRouter, Route, Switch,NavLink} from 'react-router-dom';

function App() {
  return (
    
    <BrowserRouter>
    <div className="App container">

      <h3 className="d-flex justify-content-center m-3">
        API REST Front-end.
      </h3>
        
      <nav className="navbar justify-content-center navbar-expand-sm bg-light navbar-dark">
        <ul className="navbar-nav">
          <li className="nav-item- m-1">
            <NavLink className="btn btn-light btn-outline-primary" to="/home">
              Menu Principal
            </NavLink>
          </li>

          <li className="nav-item- m-1">
            <NavLink className="btn btn-light btn-outline-primary" to="/task">
              Lista de Tareas
            </NavLink>
          </li>
          
        </ul>
      </nav>

      <Switch>
        <Route path='/home' component={Home}/>
        <Route path='/task' component={Task}/>
      </Switch>
      
    </div>
    </BrowserRouter>
  );
}

export default App;