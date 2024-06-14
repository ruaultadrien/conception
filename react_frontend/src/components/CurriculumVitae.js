import React from 'react';

function CurriculumVitae() {
    const styles = {
        container: {
            backgroundColor: '#f4f4f9',
        },
        frame: {
            maxWidth: '800px',
            margin: '70px auto',
            padding: '20px',
            backgroundColor: '#fff',
            boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
            borderRadius: '10px',
        },
        ul: {
            marginTop: 0,
            marginRight: '30px',
        },
        title: {
            color: '#003366',
            textAlign: 'center',
            fontWeight: 'bold',
            fontSize: '2em',
            marginBlockStart: '0.67em',
            marginBlockEnd: '0.67em',
        },
        subtitle: {
            color: '#006699',
            textAlign: 'center',
            fontWeight: 'bold',
            fontSize: '1.5em',
            marginBlockStart: '0.83em',
            marginBlockEnd: '0.83em',
        },
        text: {
            color: '#333',
            lineHeight: 1.6,
            margin: "0px"
        },
        section: {
            backgroundColor: '#f1f1f1',
            padding: '15px',
            borderRadius: '5px',
            marginBottom: '20px',
            marginTop: '20px',
        },
        sectionTitle: {
            color: '#004080',
            borderBottom: '2px solid #004080',
            paddingBottom: '5px',
            marginBottom: '10px',
            fontSize: '1.17em',
            fontWeight: 'bold',
        },
        itemContainer: {
            backgroundColor: '#e9edfa',
            padding: '10px',
            borderRadius: '10px',
            marginBottom: '0px',
            marginTop: '10px',
        },
        itemContainerTitle: {
            margin: 0,
            fontSize: '16px',
            fontWeight: 'bold',
        },
        educationItem: {
            backgroundColor: '#ccf2ff',
        },
    };

    return (
        <div style={styles.container}>
            <div style={styles.frame}>
                <h1 style={styles.title}>Adrien Ruault</h1>
                <h2 style={styles.subtitle}>Machine Learning Engineer</h2>

                <section>
                    <h3 style={styles.sectionTitle}>Profile</h3>
                    <p style={styles.text}>Machine Learning Engineer with 6+ years of experience, passionate about developing AI and Data solutions. Skilled in Data Science, MLOps, Cloud Engineering, Data Engineering, and Project Management. Proud to have helped grow my current company from a start-up to an established consulting business. Looking forward to connecting!</p>
                </section>

                <section>
                    <h3 style={styles.sectionTitle}>Employment History</h3>
                    <div style={styles.itemContainer}>
                        <h4 style={styles.itemContainerTitle}>Senior Machine Learning Engineer, Visium SA, Lausanne, Switzerland</h4>
                        <p style={styles.text}>October 2019 – Present | 5+ years</p>
                    </div>
                    <ul style={styles.ul}>
                        <li style={styles.text}>Delivered over 20 client projects in Data Science, MLOps, DevOps, Cloud Engineering, and Data Engineering.</li>
                        <li style={styles.text}>Provided technical leadership for several client engagements, ensuring compatibility with business requirements and successful delivery.</li>
                        <li style={styles.text}>Gained experience in various technical fields, including Natural Language Processing, Computer Vision, Time Series Forecasting, Recommender Systems, and Predictive Maintenance.</li>
                        <li style={styles.text}>Led the development of an AI SaaS product delivering recommendations based on customer baskets in online shopping.</li>
                        <li style={styles.text}>Oversaw the development of the company's internal Data Warehouse.</li>
                        <li style={styles.text}>Shaped the company's engineering operational processes as it grew from a start-up to a 60+ employee company.</li>
                    </ul>

                    <div style={styles.itemContainer}>
                        <h4 style={styles.itemContainerTitle}>Junior Machine Learning Engineer, CSEM, Neuchâtel, Switzerland</h4>
                        <p style={styles.text}>February 2019 – July 2019 | 6 months</p>
                    </div>
                    <ul style={styles.ul}>
                        <li style={styles.text}>Developed RL algorithms for controlling energy systems in buildings.</li>
                        <li style={styles.text}>Wrote a Master Thesis in the context of an MSc at EPFL.</li>
                    </ul>

                    <div style={styles.itemContainer}>
                        <h4 style={styles.itemContainerTitle}>Junior Machine Learning Engineer, SenSat, London, United Kingdom</h4>
                        <p style={styles.text}>September 2018 – February 2019 | 6 months</p>
                    </div>
                    <ul style={styles.ul}>
                        <li style={styles.text}>Developed Deep Learning Computer Vision algorithms for object detection.</li>
                        <li style={styles.text}>Worked as a full-stack developer on the company's web product.</li>
                    </ul>

                    <div style={styles.itemContainer}>
                        <h4 style={styles.itemContainerTitle}>Junior Machine Learning Engineer, Neural Concept, Lausanne</h4>
                        <p style={styles.text}>February 2018 – August 2018 | 6 months</p>
                    </div>
                    <ul style={styles.ul}>
                        <li style={styles.text}>Developed Deep Learning algorithms to predict fluid mechanics.</li>
                        <li style={styles.text}>Automated the company's generation of training examples.</li>
                    </ul>
                </section>

                <section>
                    <h3 style={styles.sectionTitle}>Education</h3>
                    <div style={{ ...styles.itemContainer, ...styles.educationItem }}>
                        <h4 style={styles.itemContainerTitle}>MSc in Computational Science and Engineering, EPFL - Ecole Polytechnique Fédérale de Lausanne, Lausanne, Switzerland</h4>
                        <p style={styles.text}>September 2016 – July 2019 | Grade: 5.44/6</p>
                    </div>

                    <div style={{ ...styles.itemContainer, ...styles.educationItem }}>
                        <h4 style={styles.itemContainerTitle}>BSc in Materials Science and Engineering, EPFL - Ecole Polytechnique Fédérale de Lausanne, Lausanne, Switzerland</h4>
                        <p style={styles.text}>September 2013 – July 2016 | Grade: 5.56/6</p>
                    </div>
                </section>

                <section style={styles.section}>
                    <h3 style={styles.sectionTitle}>Contact</h3>
                    <p style={styles.text}>Location: Lausanne, Switzerland</p>
                    <p style={styles.text}>Phone: +41 77 441 53 42</p>
                    <p style={styles.text}>Email: <a href="mailto:ruaultadrien@gmail.com" style={styles.link}>ruaultadrien@gmail.com</a></p>
                </section>

                <section style={styles.section}>
                    <h3 style={styles.sectionTitle}>Links</h3>
                    <p><a href="https://www.linkedin.com/in/adrien-ruault/" style={styles.link}>LinkedIn</a></p>
                    <p><a href="https://github.com/ruaultadrien" style={styles.link}>GitHub</a></p>
                </section>

                <section>
                    <h3 style={styles.sectionTitle}>Skills</h3>
                    <ul style={styles.ul}>
                        <li style={styles.text}><strong>Data Science:</strong> Python, TensorFlow, DVC, scikit-learn, HuggingFace</li>
                        <li style={styles.text}><strong>MLOps:</strong> Azure ML, VertexAI, TFX, MLFlow, TensorFlow Serving</li>
                        <li style={styles.text}><strong>Cloud Engineering:</strong> GCP, Azure, Terraform, CI/CD (GitHub Actions, Azure Pipelines)</li>
                        <li style={styles.text}><strong>Data Engineering:</strong> dbt, BigQuery, Snowflake, SQL, Fivetran, Databricks</li>
                        <li style={styles.text}><strong>Soft Skills:</strong> Agile Project Management, Product Development, Strategic Thinking</li>
                    </ul>
                </section>

                <section>
                    <h3 style={styles.sectionTitle}>Hobbies</h3>
                    <p style={styles.text}>Traveling across Europe on a bike, ski touring in winter, and beer brewing.</p>
                </section>

                <section>
                    <h3 style={styles.sectionTitle}>Languages</h3>
                    <ul style={styles.ul}>
                        <li style={styles.text}><strong>French</strong> - Native Speaker</li>
                        <li style={styles.text}><strong>English</strong> - Highly Proficient</li>
                        <li style={styles.text}><strong>German</strong> - Beginner</li>
                    </ul>
                </section>
            </div>
        </div>
    );
}

export default CurriculumVitae;
