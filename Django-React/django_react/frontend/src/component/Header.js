import React, {Component} from 'react';
import {Dropdown} from 'react-bootstrap';


class Header extends Component{
    constructor(props){
        super(props);
        this.state = {
        };
    }

    render(){
        return(
            <div className='Header'>
                <div className='text-center pt-4'>
                    <h1> First Website </h1>
                </div>
                <div className='d-flex flex-row float-right'>
                    <small className='align-self-center'> made by <i> Jisu </i></small>
                    <Dropdown>
                        <Dropdown.Toggle className='mybtn' id='dropdown-basic'>
                        contact
                        </Dropdown.Toggle>
                        <Dropdown.Menu>
                            <Dropdown.Item
                                href='https://github.com/JissuPark'
                                target='_blank'>Github</Dropdown.Item>
                            <Dropdown.Item
                                href='https://5w33th0me4jisu.tistory.com/'
                                target='_blank'>Tistory</Dropdown.Item>
                            <Dropdown.Item
                                href='https://www.facebook.com/profile.php?id=100027205430876'
                                target='_blank'>facebook</Dropdown.Item>
                        </Dropdown.Menu>
                    </Dropdown>
                </div>
            </div>
        );
    }
}
export default Header;