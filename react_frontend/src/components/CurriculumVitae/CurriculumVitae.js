import React from 'react';
import Contact from './Contact/Contact';
import LinksSection from './LinksSection/LinksSection';
import styles from './CurriculumVitae.module.css';

function CurriculumVitae() {
    const innerStyles = {
        frame: {
            maxWidth: '800px',
            margin: '70px auto',
            padding: '20px',
            backgroundColor: '#fff',
            boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
            borderRadius: '10px',
            fontFamily: '"Albert Sans", sans-serif',
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
        paragraph: {
            marginBottom: '1rem',
            color: '#333',
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
        <div style={innerStyles.frame}>
            <h1 style={innerStyles.title}>Adrien Ruault</h1>
            <h2 style={innerStyles.subtitle}>Machine Learning Engineer</h2>

            <section>
                <h3 className={styles.sectionTitle}>Profile</h3>
                <p style={innerStyles.paragraph}>Machine Learning Engineer with 6+ years of experience, passionate about developing AI and Data solutions. Skilled in Data Science, MLOps, Cloud Engineering, Data Engineering, and Project Management. Proud to have helped grow my current company from a start-up to an established consulting business. Looking forward to connecting!</p>
            </section>

            <section>
                <h3 className={styles.sectionTitle}>Employment History</h3>
                <div style={innerStyles.itemContainer}>
                    <h4 style={innerStyles.itemContainerTitle}>Senior Machine Learning Engineer, Visium SA, Lausanne, Switzerland</h4>
                    <p className={styles.text}>October 2019 – Present | 5+ years</p>
                </div>
                <ul style={innerStyles.ul}>
                    <li className={styles.text}>Delivered over 20 client projects in Data Science, MLOps, DevOps, Cloud Engineering, and Data Engineering.</li>
                    <li className={styles.text}>Provided technical leadership for several client engagements, ensuring compatibility with business requirements and successful delivery.</li>
                    <li className={styles.text}>Gained experience in various technical fields, including Natural Language Processing, Computer Vision, Time Series Forecasting, Recommender Systems, and Predictive Maintenance.</li>
                    <li className={styles.text}>Led the development of an AI SaaS product delivering recommendations based on customer baskets in online shopping.</li>
                    <li className={styles.text}>Oversaw the development of the company's internal Data Warehouse.</li>
                    <li className={styles.text}>Shaped the company's engineering operational processes as it grew from a start-up to a 60+ employee company.</li>
                </ul>

                <div style={innerStyles.itemContainer}>
                    <h4 style={innerStyles.itemContainerTitle}>Junior Machine Learning Engineer, CSEM, Neuchâtel, Switzerland</h4>
                    <p className={styles.text}>February 2019 – July 2019 | 6 months</p>
                </div>
                <ul style={innerStyles.ul}>
                    <li className={styles.text}>Developed RL algorithms for controlling energy systems in buildings.</li>
                    <li className={styles.text}>Wrote a Master Thesis in the context of an MSc at EPFL.</li>
                </ul>

                <div style={innerStyles.itemContainer}>
                    <h4 style={innerStyles.itemContainerTitle}>Junior Machine Learning Engineer, SenSat, London, United Kingdom</h4>
                    <p className={styles.text}>September 2018 – February 2019 | 6 months</p>
                </div>
                <ul style={innerStyles.ul}>
                    <li className={styles.text}>Developed Deep Learning Computer Vision algorithms for object detection.</li>
                    <li className={styles.text}>Worked as a full-stack developer on the company's web product.</li>
                </ul>

                <div style={innerStyles.itemContainer}>
                    <h4 style={innerStyles.itemContainerTitle}>Junior Machine Learning Engineer, Neural Concept, Lausanne</h4>
                    <p className={styles.text}>February 2018 – August 2018 | 6 months</p>
                </div>
                <ul style={innerStyles.ul}>
                    <li className={styles.text}>Developed Deep Learning algorithms to predict fluid mechanics.</li>
                    <li className={styles.text}>Automated the company's generation of training examples.</li>
                </ul>
            </section>

            <section>
                <h3 className={styles.sectionTitle}>Education</h3>
                <div style={{ ...innerStyles.itemContainer, ...innerStyles.educationItem }}>
                    <h4 style={innerStyles.itemContainerTitle}>MSc in Computational Science and Engineering, EPFL - Ecole Polytechnique Fédérale de Lausanne, Lausanne, Switzerland</h4>
                    <p className={styles.text}>September 2016 – July 2019 | Grade: 5.44/6</p>
                </div>

                <div style={{ ...innerStyles.itemContainer, ...innerStyles.educationItem }}>
                    <h4 style={innerStyles.itemContainerTitle}>BSc in Materials Science and Engineering, EPFL - Ecole Polytechnique Fédérale de Lausanne, Lausanne, Switzerland</h4>
                    <p className={styles.text}>September 2013 – July 2016 | Grade: 5.56/6</p>
                </div>
            </section>

            <div className={styles.containerContactLinks}>
                <Contact />
                <LinksSection />
            </div>


            <section>
                <h3 className={styles.sectionTitle}>Skills</h3>
                <ul style={innerStyles.ul}>
                    <li className={styles.text}><strong>Data Science:</strong> Python, TensorFlow, DVC, scikit-learn, HuggingFace</li>
                    <li className={styles.text}><strong>MLOps:</strong> Azure ML, VertexAI, TFX, MLFlow, TensorFlow Serving</li>
                    <li className={styles.text}><strong>Cloud Engineering:</strong> GCP, Azure, Terraform, CI/CD (GitHub Actions, Azure Pipelines)</li>
                    <li className={styles.text}><strong>Data Engineering:</strong> dbt, BigQuery, Snowflake, SQL, Fivetran, Databricks</li>
                    <li className={styles.text}><strong>Soft Skills:</strong> Agile Project Management, Product Development, Strategic Thinking</li>
                </ul>
            </section>

            <section>
                <h3 className={styles.sectionTitle}>Hobbies</h3>
                <p style={innerStyles.paragraph}>Traveling across Europe on a bike, ski touring in winter, and beer brewing.</p>
            </section>

            <section>
                <h3 className={styles.sectionTitle}>Languages</h3>
                <ul style={innerStyles.ul}>
                    <li className={styles.text}><strong>French</strong> - Native Speaker</li>
                    <li className={styles.text}><strong>English</strong> - Highly Proficient</li>
                    <li className={styles.text}><strong>German</strong> - Beginner</li>
                </ul>
            </section>
        </div>
    );
}

export default CurriculumVitae;
