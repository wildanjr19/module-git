const path = require("path");

module.exports = {
  basedir: __dirname,
  stylesheet: [path.join(__dirname, "pdf-style.css")],
  pdf_options: {
    format: "A4",
    margin: "18mm 14mm 22mm 16mm",
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: `
      <style>
        .date, .title, .url { display: none; }
      </style>
      <div></div>
    `,
    footerTemplate: `
      <style>
        html, body {
          margin: 0;
          padding: 0;
          width: 100%;
          font-size: 9px;
          color: #64748b;
        }
        .date, .title, .url {
          display: none;
        }
        .footer {
          width: 100%;
          padding: 0 16mm 0 14mm;
          text-align: center;
          box-sizing: border-box;
        }
      </style>
      <div class="footer">
        Halaman <span class="pageNumber"></span> dari <span class="totalPages"></span>
      </div>
    `,
  },
};
