import fb from './download.png'
import github from './github.png'
import insta from './instagram.jpg'
import twit from './twitter.png'
import linked from './linkedin.jpg'

export default function Footer(){
    return(
        <footer className='foot'>
            <img  src = {twit} />
            <img  src = {fb} />
            <img  src = {insta} />
            <img  src = {linked} />
            <img  src = {github} />
        </footer>
    )
}