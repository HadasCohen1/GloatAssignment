
import Badge from 'react-bootstrap/Badge';
import './Candidate.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBriefcase } from '@fortawesome/free-solid-svg-icons'
import { faCheck } from '@fortawesome/free-solid-svg-icons'
import { faTimes } from '@fortawesome/free-solid-svg-icons'
import { faCheckCircle } from '@fortawesome/free-solid-svg-icons'
import Button from 'react-bootstrap/Button';
import { useState } from 'react';
import axios from "axios";
import cookie from "react-cookies";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

function Position(props) {
    const element = <FontAwesomeIcon icon={faBriefcase} />;
    const checkIcon = <FontAwesomeIcon icon={faCheck} />;
    const declineIcon = <FontAwesomeIcon icon={faTimes} />;
    const checkCircle = <FontAwesomeIcon icon={faCheckCircle} />;

    const [applied, setApplied] = useState(false);
    const apply = () => setApplied(true);
    return (
        <div className="position">
            <div style={{ paddingRight: '10px' }}>{element} </div>
            <div className='job'>
                <div> {props.job.title} - {props.job.skill.name}</div>
                <div className="reason">{props.reason}</div>

            </div>
            {!applied ? (<div>
                <Button onClick={apply} className={applied ? "selected" : ""} style={{ marginRight: '5px' }} variant="light" size="sm">{checkIcon} Apply</Button>
                <Button onClick={() => { props.positionDecline(props.id) }} variant="light" size="sm">{declineIcon} Decline</Button>
            </div>) : <div className="applied">{checkCircle} Request Sent</div>}
        </div>
    );
}


function Candidate(props) {
    let skills = props.candidate.skills || [];
    const [positions, setPositions] = useState(props.candidate.matches);
    const onPositionDecline = positionId => {
        
        axios.delete(`/api/match/${positionId}/`, {headers: {"X-CSRFTOKEN": cookie.load("csrftoken")}})
            .then(
                (result) => {
                    setPositions(positions.filter(p => p.id !== positionId));
                },
                (error) => {
                    console.log(error);
                }
            )
    }
    let pos = positions.map(p => { return <Position key={p['id']} id={p.id} job={p['job']} reason={p['reason']} positionDecline={onPositionDecline}></Position> });
    return (
        <div className="candidate">
            <div className="candidate-details">
                <div className="title" style={{ paddingBottom: '0.5rem' }}>{props.candidate.title}</div>
                <div className="skils">{skills.map(s => <Badge key={s.id} style={{ marginRight: '5px' }} variant="light">{s.name}</Badge>)}</div>
            </div>
            <div style={{ textAlign: 'center' }}>Suggested Positions:</div>
            <div>
                {pos}
            </div>
        </div>
    );
};

export default Candidate