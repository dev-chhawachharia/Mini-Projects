export default function Header(){
    return(
        <header className="header-bar">
            <img src={require("./planet-earth.png")}  alt = "Black and White globe" className="header-img"/>
            <p className="header-txt">My Travel Journal</p>
        </header>
    )
}