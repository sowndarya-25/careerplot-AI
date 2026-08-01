import { Menu } from "lucide-react";

const Navbar = () => {

  const navLinks=[
    {name:"Home",id:"home"},
    {name:"Features",id:"features"},
    {name:"AI Tools",id:"tools"},
    {name:"Testimonials",id:"testimonials"}
  ];

  const scrollToSection=(id)=>{
      document.getElementById(id)?.scrollIntoView({
        behavior:"smooth"
      });
  };

  return(

<header className="fixed top-0 left-0 w-full z-50 backdrop-blur-xl bg-black/40 border-b border-emerald-500/10">

<div className="max-w-7xl mx-auto px-8 h-20 flex justify-between items-center">

<div className="text-3xl font-black tracking-tight">

Career<span className="text-emerald-400">Pilot</span>

</div>

<nav className="hidden md:flex gap-10">

{

navLinks.map((item)=>(

<button

key={item.id}

onClick={()=>scrollToSection(item.id)}

className="text-gray-300 hover:text-emerald-400 transition duration-300"

>

{item.name}

</button>

))

}

</nav>

<div className="flex items-center gap-4">

<button

className="px-5 py-2 rounded-xl border border-emerald-500 text-emerald-400 hover:bg-emerald-500 hover:text-black transition"

>

Login

</button>

<button

className="bg-emerald-400 text-black px-6 py-2 rounded-xl font-semibold hover:scale-105 transition"

>

Get Started

</button>

<Menu className="md:hidden"/>

</div>

</div>

</header>

  );

};

export default Navbar;