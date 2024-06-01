import './App.css';

function App() {
  return (
    <div class="container">
        <h1>Adrien Ruault</h1>
        <h2>Machine Learning Engineer</h2>
        
        <section>
            <h3 class="section-title">Profile</h3>
            <p>Machine Learning Engineer with 6+ years of experience, passionate about developing AI and Data solutions. Skilled in Data Science, MLOps, Cloud Engineering, Data Engineering, and Project Management. Proud to have helped grow my current company from a start-up to an established consulting business. Looking forward to connecting!</p>
        </section>

        <section>
            <h3 class="section-title">Employment History</h3>
            <div class="item-container">
                <h4>Senior Machine Learning Engineer, Visium SA, Lausanne, Switzerland</h4>
                <p>October 2019 – Present</p>
            </div>
            <ul>
                <li>Delivered over 20 client projects in Data Science, MLOps, DevOps, Cloud Engineering, and Data Engineering.</li>
                <li>Provided technical leadership for several client engagements, ensuring compatibility with business requirements and successful delivery.</li>
                <li>Gained experience in various technical fields, including Natural Language Processing, Computer Vision, Time Series Forecasting, Recommender Systems, and Predictive Maintenance.</li>
                <li>Led the development of an AI SaaS product delivering recommendations based on customer baskets in online shopping.</li>
                <li>Oversaw the development of the company's internal Data Warehouse.</li>
                <li>Shaped the company's engineering operational processes as it grew from a start-up to a 60+ employee company.</li>
            </ul>

            <div class="item-container">
                <h4>Junior Machine Learning Engineer, CSEM, Neuchâtel, Switzerland</h4>
                <p>February 2019 – July 2019</p>
            </div>
            <ul>
                <li>Developed RL algorithms for controlling energy systems in buildings.</li>
                <li>Wrote a Master Thesis in the context of an MSc at EPFL.</li>
            </ul>

            <div class="item-container">
                <h4>Junior Machine Learning Engineer, SenSat, London, United Kingdom</h4>
                <p>September 2018 – February 2019</p>
            </div>
            <ul>
                <li>Developed Deep Learning Computer Vision algorithms for object detection.</li>
                <li>Worked as a full-stack developer on the company's web product.</li>
            </ul>

            <div class="item-container">
                <h4>Junior Machine Learning Engineer, Neural Concept, Lausanne</h4>
                <p>February 2018 – August 2018</p>
            </div>
            <ul>
                <li>Developed Deep Learning algorithms to predict fluid mechanics.</li>
                <li>Automated the company's generation of training examples.</li>
            </ul>
        </section>

        <section>
            <h3 class="section-title">Education</h3>
            <div class="item-container education-item">
                <h4>MSc in Computational Science and Engineering, EPFL - Ecole Polytechnique Fédérale de Lausanne, Lausanne, Switzerland</h4>
                <p>September 2016 – July 2019 | Grade: 5.44/6</p>
            </div>

            <div class="item-container education-item">
                <h4>BSc in Materials Science and Engineering, EPFL - Ecole Polytechnique Fédérale de Lausanne, Lausanne, Switzerland</h4>
                <p>September 2013 – July 2016 | Grade: 5.56/6</p>
            </div>
        </section>

        <section class="contact">
            <h3 class="section-title">Contact</h3>
            <p>Location: Lausanne, Switzerland</p>
            <p>Phone: +41 77 441 53 42</p>
            <p>Email: <a href="mailto:ruaultadrien@gmail.com">ruaultadrien@gmail.com</a></p>
        </section>

        <section class="links">
            <h3 class="section-title">Links</h3>
            <p><a href="https://www.linkedin.com/in/adrien-ruault/">LinkedIn</a></p>
            <p><a href="https://github.com/ruaultadrien">GitHub</a></p>
        </section>

        <section class="skills">
            <h3 class="section-title">Skills</h3>
            <ul>
                <li><strong>Data Science:</strong> Python, TensorFlow, DVC, scikit-learn, HuggingFace</li>
                <li><strong>MLOps:</strong> Azure ML, VertexAI, TFX, MLFlow, TensorFlow Serving</li>
                <li><strong>Cloud Engineering:</strong> GCP, Azure, Terraform, CI/CD (GitHub Actions, Azure Pipelines)</li>
                <li><strong>Data Engineering:</strong> dbt, BigQuery, Snowflake, SQL, Fivetran, Databricks</li>
                <li><strong>Soft Skills:</strong> Agile Project Management, Product Development, Strategic Thinking</li>
            </ul>
        </section>

        <section class="hobbies">
            <h3 class="section-title">Hobbies</h3>
            <p>Traveling across Europe on a bike, ski touring in winter, and beer brewing.</p>
        </section>

        <section class="languages">
            <h3 class="section-title">Languages</h3>
            <ul>
                <li>French</li>
                <li>English</li>
                <li>German</li>
            </ul>
        </section>
    </div>
  );
}

export default App;
