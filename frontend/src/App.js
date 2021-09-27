import React from "react";
import axios from "axios";
import logo from './logo.svg';
import './App.css';
import UsersList from "./components/Users";
import Menu from "./components/Menu";
import Footer from "./components/Footer";

class App extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            'users': []
        }
    }
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data
                this.setState({
                    'users': users
                }
                )
            })
            .catch(error => console.log(error))
    }

    render() {
        const bodyStyle = {
            display: 'flex'
        }
        const usersList = {
            padding: ('100px')
        }
        const headerStyle = {
        }
        const footerStyle = {
            position: 'absolute',
            bottom: 0
        }
        return(
            <div style={bodyStyle}>
                <div style={headerStyle}>
                    <Menu/>
                </div>

                <div style={usersList}>
                    <UsersList users={this.state.users}/>
                </div>

                <div style={footerStyle}>
                    <Footer/>
                </div>
            </div>
        )
    }
}
//
// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

export default App;
