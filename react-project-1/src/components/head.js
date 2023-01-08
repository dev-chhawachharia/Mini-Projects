import self_img from "./IMG_20220816_231903_249.jpg"
export default function Head(){
    return(
        <div className='head-container'>
            <img src = {self_img}  alt="Image" className = 'head-img'/>
        </div>
    );
}