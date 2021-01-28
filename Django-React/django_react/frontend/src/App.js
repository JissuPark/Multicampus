import './App.css';
import React, { Component } from 'react';
// bootstrap
import 'bootstrap/dist/css/bootstrap.min.css';
// link
import {BrowserRouter as Router} from 'react-router-dom';
// axios
import axios from 'axios';
//component
import MyNav from './component/Nav';
import Main from './component/Main';

class App extends Component  {
    constructor(props){
        super(props);
        this.state = {
            posts: [],
            isloading: true
        };
    }
    getpost = async() => {
        const {data}= await axios.get('http://127.0.0.1:8000/');
        this.setState({posts:{data}.data});
        this.setState({isloading: false});
    }
    async componentDidMount() {
       this.getpost();
    }

    render() {
        const {isloading} = this.state;
        const {posts} = this.state;
        return (
                <Router>
                    {isloading? 'not yet':
                        <>
                            <MyNav apps={posts}/>
                            <Main/>
                        </>
                    }
                </Router>
        );
    }
}
export default App;
