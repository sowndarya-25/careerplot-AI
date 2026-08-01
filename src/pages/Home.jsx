import Navbar from "../components/common/Navbar";

const Home=()=>{

return(

<div className="bg-[#050505] text-white">

<Navbar/>

<section

id="home"

className="min-h-screen flex justify-center items-center"

>

<h1 className="text-6xl font-bold">

Career<span className="text-emerald-400">Pilot</span>

</h1>

</section>

<section
id="features"
className="min-h-screen flex justify-center items-center"
>

<h2 className="text-5xl">

Features

</h2>

</section>

<section
id="tools"
className="min-h-screen flex justify-center items-center"
>

<h2 className="text-5xl">

AI Tools

</h2>

</section>

<section
id="testimonials"
className="min-h-screen flex justify-center items-center"
>

<h2 className="text-5xl">

Testimonials

</h2>

</section>

</div>

);

};

export default Home;