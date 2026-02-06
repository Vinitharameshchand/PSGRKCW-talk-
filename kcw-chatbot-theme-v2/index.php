<?php get_header(); ?>

<header style="background:#7a0026;padding:15px;color:#fff">
  <h2>KCW</h2>
  <nav>
    <a href="#" style="color:#fff;margin-right:15px">Home</a>
    <a href="#" style="color:#fff;margin-right:15px">About Us</a>
    <a href="#" style="color:#fff;margin-right:15px">Departments</a>
    <a href="#" style="color:#fff;margin-right:15px">Gallery</a>
    <a href="#" style="color:#fff">Contact</a>
  </nav>
</header>

<section style="padding:40px;max-width:1100px;margin:auto" id="pageContent">

<p>
KCW is an autonomous college of higher education for women. It is affiliated to the Bharathiar University, Coimbatore, ranked #9 among colleges in India in NIRF, accredited with the highest A++ grade by NAAC, and a UGC-certified ‘College of Excellence’. Serving 8,500+ students with 400+ faculty, KCW is recognised for its impact on society through its academic programmes, holistic approach, community outreach, and an enduring vision for the future.
</p>

<p>
The journey has not been easy. It has demanded dedication and commitment to a purpose, unbridled passion and perseverance, and an indomitable spirit of entrepreneurship. From being the first college in Tamil Nadu to introduce the BCom programme for women to establishment of an MBA programme for women in 1993, KCW has been a trailblazer. Accredited by NAAC first in 2001, KCW currently enjoys A++ grade in its 4th cycle. Autonomous status was granted in 2004 and College of Excellence status in 2016.
</p>

<p>
During this period, KCW established specialised centres for Gandhian Studies, Ambedkar Studies and Women Studies. All science departments have been granted ‘Star’ status by DST.
</p>

<p>
KCW celebrated its golden jubilee in 2013. Subsequent initiatives include the Rural Women Technology Park, Food Quality Testing Laboratory, Centres of Excellence, Digital Innovation Dojo (with Elgi), Centre for Women Leadership, and GRG Gen Next Foundation.
</p>

<p>
KCW has international collaborations with universities in the USA, UK, Mexico, Tanzania, and Malaysia, facilitating study-abroad programmes, faculty and student mobility, and collaborative research.
</p>

</section>

<!-- CHATBOT -->
<div id="chat-toggle" style="position:fixed;bottom:20px;right:20px;background:#7a0026;color:#fff;width:60px;height:60px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer">💬</div>

<div id="chatbot" style="display:none;position:fixed;bottom:20px;right:20px;width:340px;background:#fff;border-radius:12px;box-shadow:0 0 15px rgba(0,0,0,.3);flex-direction:column;z-index:9999">
  <div id="chat-header" style="background:#7a0026;color:#fff;padding:10px;cursor:pointer;font-weight:bold">KCW Assistant</div>
  <div id="chat-body" style="padding:10px;height:260px;overflow-y:auto;font-size:14px"></div>
  <div style="display:flex;border-top:1px solid #ccc">
    <input id="userInput" style="flex:1;padding:8px;border:none" placeholder="Ask about KCW...">
    <button onclick="askBot()" style="background:#7a0026;color:#fff;border:none;padding:8px">Send</button>
  </div>
</div>

<script>
const faqData = [
 {keys:["autonomous","ugc"],ans:"KCW is an autonomous college granted autonomy by UGC in 2004 and affiliated with Bharathiar University."},
 {keys:["ranking","rank","naac","nirf","grade","accreditation"],ans:"KCW is ranked #9 in India (NIRF) and accredited with the highest A++ grade by NAAC."},
 {keys:["students","faculty","strength"],ans:"KCW serves over 8,500 students supported by more than 400 faculty members."},
 {keys:["bcom","mba","programme","milestone"],ans:"KCW was the first in Tamil Nadu to introduce BCom for women and established an MBA programme for women in 1993."},
 {keys:["centre","centres","studies","dst","star"],ans:"KCW has centres for Gandhian Studies, Ambedkar Studies and Women Studies. All science departments have DST Star status."},
 {keys:["golden","jubilee","2013"],ans:"KCW celebrated its golden jubilee in 2013 with pride and fulfilment."},
 {keys:["innovation","dojo","leadership","startup"],ans:"KCW established Digital Innovation Dojo with Elgi, Centre for Women Leadership, and GRG Gen Next Foundation."},
 {keys:["international","foreign","collaboration","abroad","university"],ans:"KCW collaborates with universities in the USA, UK, Mexico, Tanzania, and Malaysia for global exposure and research."}
];

const suggested = [
 "Is KCW autonomous?",
 "What is the NAAC grade of KCW?",
 "How many students study in KCW?",
 "What milestones has KCW achieved?",
 "Does KCW have international collaborations?"
];

const chatBody = document.getElementById("chat-body");

function loadSuggestions(){
 let html="<strong>Suggested Questions</strong><br>";
 suggested.forEach(q=>{
  html+=`<button style="margin:4px;padding:6px 10px;border-radius:20px;border:1px solid #7a0026;background:#fff;color:#7a0026;cursor:pointer;font-size:12px" onclick="autoAsk('${q}')">${q}</button>`;
 });
 chatBody.innerHTML=html;
}

function findAnswer(q){
 q=q.toLowerCase();
 let best=null,score=0;
 faqData.forEach(f=>{
  let s=0;
  f.keys.forEach(k=>{ if(q.includes(k)) s++; });
  if(s>score){ score=s; best=f.ans; }
 });
 return best || "You can ask about KCW autonomy, ranking, milestones, centres, students, or international collaborations.";
}

function askBot(){
 const i=document.getElementById("userInput");
 const q=i.value.trim();
 if(!q) return;
 chatBody.innerHTML+=`<p><b>You:</b> ${q}</p>`;
 chatBody.innerHTML+=`<p><b>KCW Bot:</b> ${findAnswer(q)}</p>`;
 chatBody.scrollTop=chatBody.scrollHeight;
 i.value="";
}

function autoAsk(q){
 document.getElementById("userInput").value=q;
 askBot();
}

document.getElementById("chat-toggle").onclick=()=>{
 document.getElementById("chatbot").style.display="flex";
 document.getElementById("chat-toggle").style.display="none";
 loadSuggestions();
};

document.getElementById("chat-header").onclick=()=>{
 document.getElementById("chatbot").style.display="none";
 document.getElementById("chat-toggle").style.display="flex";
};
</script>

<?php get_footer(); ?>
