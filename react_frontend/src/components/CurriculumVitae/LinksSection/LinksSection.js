import React from 'react';
import styles from '../CurriculumVitae.module.css'
const LinksSection = () => {

    return (
        <div className={styles.linksSection}>
            <section className={styles.section}>
                <h3 className={styles.sectionTitle}>Links</h3>
                <p><a href="https://www.linkedin.com/in/adrien-ruault/" className={styles.link}>LinkedIn</a></p>
                <p><a href="https://github.com/ruaultadrien" className={styles.link}>GitHub</a></p>
            </section>
        </div>
    );
}

export default LinksSection;