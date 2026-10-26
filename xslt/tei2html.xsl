<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:tei="http://www.tei-c.org/ns/1.0"
    exclude-result-prefixes="tei">

  <xsl:output method="html" encoding="UTF-8" indent="yes"
              doctype-system="about:legacy-compat"/>

  <xsl:template match="/tei:TEI">
    <html lang="en">
      <head>
        <title>
          <xsl:value-of select="tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title"/>
        </title>
        <link rel="stylesheet" href="../css/style.css"/>
      </head>
      <body>
        <main class="container">
          <h1>
            <xsl:value-of select="tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title"/>
          </h1>
          <!-- TODO: templates for tei:text/tei:body -->
        </main>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>
