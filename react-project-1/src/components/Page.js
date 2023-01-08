import Head from "./head.js"
import Main from "./Main.js"
import Footer from "./Footer.js"

export default function Page(){
    return(
        <div className = 'page'>
            <Head />
            <Main />
            <Footer />
        </div>
    )
}