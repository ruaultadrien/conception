import React from 'react';
import styles from '../CurriculumVitae.module.css'

const Contact = () => {
    return (
        <section className={styles.section}>
            <h3 className={styles.sectionTitle}>Contact</h3>
                <p className={styles.text}>Location: Lausanne, Switzerland</p>
                <p className={styles.text}>Phone: +41 77 441 53 42</p>
                <p className={styles.text}>Email: <a href="mailto:ruaultadrien@gmail.com" className={styles.link}>ruaultadrien@gmail.com</a></p>
        </section>
    );
}

export default Contact;