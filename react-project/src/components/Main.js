export default function Main(props){
    // let myStyle;
    // if(props.item.id % 2 == 0 )
    //     myStyle = {
    //         float: "right"
    //     }
    // else 
    // myStyle = {
    //     float: "left"
    // }
    return(
        <div className="main-div">
            <img  src = {props.item.imageUrl} className="main-img" />
            <p className = "main-country"> 📍 {props.item.location.toUpperCase()} <a href={props.item.googleMapsUrl} className= "main-link">View on Google Map</a></p>
            <h1 className="main-title">{props.item.title}</h1>
            <h3 className="main-date">{props.item.startDate} - {props.item.endDate}</h3>
            <p className="main-desc">{props.item.description}</p>
        </div>
    )
}