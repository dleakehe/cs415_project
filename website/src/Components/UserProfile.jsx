import React, {useState, useEffect} from 'react'
import { useNavigate } from "react-router-dom"
import "bootstrap/dist/css/bootstrap.min.css";
import { MDBContainer, MDBRow, MDBCol } from "mdb-react-ui-kit";


const UserProfile = () => {
    const navigate = useNavigate();
    const [userColumns, setUserColumns] = useState([]);
    const [record, setRecord] = useState([]);
    const [players, setPlayers]  = useState([]);
    const [playersColumns, setPlayersColumns] = useState([]);
    const user_id = window.sessionStorage.getItem("user_id");


    useEffect(() => {
        if (!window.sessionStorage.getItem("auth")) navigate('/unauthorized')
        fetch('http://localhost:8000/users/user/' + user_id)
        .then(res => res.json())
        .then(data => {
            console.log(data)
            setUserColumns(Object.keys(data.user))
            setRecord(data.user)
            setPlayersColumns(Object.keys(data.characters[0]))
            setPlayers(data.characters)
        })
        .catch(error => console.error(error));
    }, []);

    const handleLogout = (e) => {
        e.preventDefault();
        window.sessionStorage.removeItem("auth")
        window.sessionStorage.removeItem("user_id")
        window.sessionStorage.removeItem("token")
        navigate('/login')
    }

  return (
    <div>
        <br />
        <div className="page shadow">
            <div className="main-container shadow">
                <MDBContainer>
                <br />
                    <MDBRow>
                        <MDBCol>
                            <div className="container">
                            </div>
                        </MDBCol>
                    </MDBRow>
                    <MDBRow>
                        <MDBCol>
                            <div class="container">
                                <h3>{record.first_name} {record.last_name}</h3>
                            </div>

                        </MDBCol>
                    </MDBRow>
                    <MDBRow>
                        <table className='user-table'>
                            <thead>
                                <tr>
                                    <th key="1">USER ID</th>
                                    <th key="2">EMAIL</th>
                                    <th key="4">LAST LOGIN</th>

                                </tr>
                            </thead>
                            <tbody>
                                {
                                    <tr key={record.user_id}>
                                        <td>{record.user_id}</td>
                                        <td>{record.email}</td>
                                        <td>{new Date(record.last_login).toLocaleString()}</td>
                                    </tr>
                                }
                            </tbody>
                        </table>
                    </MDBRow>
                    <br />
                </MDBContainer>
            </div>
        </div>

         <br />  

        <h2>Characters</h2>
        <table className='user-table'>
            <thead>
                <tr>
                    <th>NAME</th>
                    <th>LEVEL</th>
                    <th>CLASS</th>
                    <th>RACE</th>
                    <th>SKILL 1</th>
                    <th>SKILL 2</th>
                    <th>SKILL 3</th>
                </tr>
            </thead>
            <tbody>
                {
                    players.map((players,i) => (
                    <tr key={players.user_id}>
                        <td>{players.charname}</td>
                        <td>{players.level}</td>
                        <td>{players.class_field}</td>
                        <td>{players.race}</td>
                        <td>{players.skill1}</td>
                        <td>{players.skill2}</td>
                        <td>{players.skill3}</td>
                    </tr>
                    ))
                }
            </tbody>
        </table>  
        <button className="login-button" onClick={handleLogout}>Logout</button>
    </div>
  )
}

export default UserProfile