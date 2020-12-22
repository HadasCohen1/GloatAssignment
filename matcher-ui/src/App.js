import './App.css';
import Candidate from './Candidate.js';
import axios from "axios";
import { useState, createRef } from 'react';
import ClipLoader from "react-spinners/ClipLoader";
import Navbar from "react-bootstrap/Navbar";
import InputGroup from "react-bootstrap/InputGroup"
import FormControl from "react-bootstrap/FormControl"
import Button from "react-bootstrap/Button"
import { faArrowRight } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'


function Login(props) {
  let textInput = createRef();

  return (
    <div className="login">
      <InputGroup className="mb-3">
        <FormControl ref={textInput}
          placeholder="Candidate's name"
          aria-label="Candidate's name"
        />
        <InputGroup.Append>
          <Button onClick={() => { props.login(textInput.current.value) }} variant="outline-secondary">< FontAwesomeIcon icon={faArrowRight} /></Button>
        </InputGroup.Append>
      </InputGroup>
    </div>
  );
}


function App() {
  const [isLoading, setLoading] = useState(false);
  const [loggedIn, setLogin] = useState({ user: null, candidate: null });

  // get candidate data and suggested postions
  const login = username => {
    setLoading(true);
    axios.get(`/api/candidate/?username=${username}`)
      .then(
        (result) => {
          if (result.data.length) {
            setLogin({ user: username, candidate: result.data[0] });
          }
          setLoading(false);
        },
        (error) => {
          console.log(error);
          setLoading(false);
        }
      )
  }

  const loading = <div className="loader"><ClipLoader size={150} color={"#123abc"} loading={isLoading} /></div>;

  const handleLogout = () => {
    if (loggedIn.user) {
      setLogin({ user: null, candidate: null });
    }
  };
  return (
    <div className="App">
      <Navbar className="nav">
        <Navbar.Brand>Candidate Finder</Navbar.Brand>
        <Navbar.Toggle />
        <Navbar.Collapse className="justify-content-end">
          <Navbar.Text style={{ paddingRight: '5px', color: 'black', fontWeight: 'bold' }}>
            {loggedIn.user ? loggedIn.user : ''}
          </Navbar.Text>
          <Navbar.Text onClick={handleLogout} style={{ cursor: 'pointer' }}>
            {loggedIn.user ? 'logout' : 'login'}
          </Navbar.Text>
        </Navbar.Collapse>
      </Navbar>
      <div className="app-content">
        {!isLoading ? (loggedIn.user ?
          <div>
            <Candidate key={loggedIn.candidate.id} candidate={loggedIn.candidate}></Candidate>
          </div>
          : <Login login={login}></Login>) : loading}
      </div>
    </div>
  );
}

export default App;
