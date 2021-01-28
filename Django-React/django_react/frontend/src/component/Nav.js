import {Link} from 'react-router-dom';
import React,{Component} from 'react';
import {Navbar, Nav} from 'react-bootstrap';

class MyNav extends Component {
    constructor(props){
        super(props);
        this.state={
            app_info:props.apps
        };
    }

    render(){
        return(
            <Navbar bg='dark' variant='dark' className="flex-column ">
                <Navbar.Brand href='/' className='mr-0'>
                    <pre className='text-reset mt-3'>
                        <h2>{`Django-React\n  Project`}</h2>
                    </pre>
                </Navbar.Brand>
                <Nav className='flex-column'>
                    {this.state.app_info.map(item => (
                        <Link key={item.id} to={item.name}  className='nav-link'>
                            <h3>{item.name}</h3>
                        </Link>
                    ))}
                </Nav>
            </Navbar>
        );
    }


}

export default MyNav;

