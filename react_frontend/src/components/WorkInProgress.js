// src/WorkInProgress.js

import React from 'react';

const WorkInProgress = () => {
    const containerStyle = {
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
        backgroundColor: '#f4f4f9',
        color: '#003366',
        textAlign: 'center',
    };

    const titleStyle = {
        fontSize: '3em',
        marginBottom: '0.5em',
        color: '#004080'
    };

    const subtitleStyle = {
        fontSize: '1.5em',
        color: '#006699'
    };

    const loaderStyle = {
        marginTop: '1em',
        borderTop: '16px solid #004080',
        borderRight: '16px solid #f4f4f9',
        borderBottom: '16px solid #004080',
        borderLeft: '16px solid #f4f4f9',
        borderRadius: '50%',
        width: '120px',
        height: '120px',
        animation: 'spin 2s linear infinite'
    };

    const keyframes = `
    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
  `;

    return (
        <div style={containerStyle}>
            <style>{keyframes}</style>
            <h1 style={titleStyle}>Work in Progress</h1>
            <p style={subtitleStyle}>We're working hard to bring you something amazing. Stay tuned!</p>
            <div style={loaderStyle}></div>
        </div>
    );
};

export default WorkInProgress;
