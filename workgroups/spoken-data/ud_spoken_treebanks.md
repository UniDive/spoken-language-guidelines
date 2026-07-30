---
layout: base
title:  'List of current spoken treebanks'
udver: '2'
---

# Current spoken treebanks

This page is a slim recap generated from per-treebank data files in [`workgroups/spoken-data/treebanks/`](https://github.com/UniDive/spoken-language-guidelines/tree/main/workgroups/spoken-data/treebanks). Each treebank has its own page with full metadata review details and a manual-check list. Advice references the standardized naming conventions in [Metadata harmonisation](metadata.html). Use the search box, filters, or click a column header to sort.

<div id="tb-controls">
  <input type="text" id="tb-search" placeholder="Search treebank name..." />
  <select id="tb-type-filter">
    <option value="">All types</option>
      <option value="mixed">mixed</option>
      <option value="only spoken">only spoken</option>
  </select>
  <select id="tb-ident-filter">
    <option value="">Spoken identifiable: any</option>
      <option value="n/a">n/a</option>
      <option value="no">no</option>
      <option value="not assessed">not assessed</option>
      <option value="yes">yes</option>
  </select>
  <label><input type="checkbox" id="tb-todo-only" /> only treebanks with open items</label>
  <span id="tb-count"></span>
</div>

<table id="tb-table">
  <thead>
    <tr>
      <th data-col="0" data-type="string">treebank</th>
      <th data-col="1" data-type="string">type</th>
      <th data-col="2" data-type="number">sentences</th>
      <th data-col="3" data-type="number">tokens</th>
      <th data-col="4" data-type="string">spoken identifiable?</th>
      <th data-col="5" data-type="number">document-level</th>
      <th data-col="6" data-type="number">speaker-level</th>
      <th data-col="7" data-type="number">sentence-level</th>
      <th data-col="8" data-type="number">token-level</th>
      <th data-col="9" data-type="number">items to check</th>
      <th data-col="10" data-type="string">issue draft</th>
    </tr>
  </thead>
  <tbody>
      <tr data-type="only spoken" data-ident="n/a" data-todo="0">
        <td><a href="treebanks/UD_Abaza-ATB.html">Abaza ATB</a></td>
        <td>only spoken</td>
        <td class="num">98</td>
        <td class="num">652</td>
        <td>n/a</td>
        <td class="num">3</td>
        <td class="num">1</td>
        <td class="num">2</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td><a href="issue_drafts/UD_Abaza-ATB.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="yes" data-todo="0">
        <td><a href="treebanks/UD_Alemannic-DIVITAL.html">Alemannic DIVITAL</a></td>
        <td>mixed</td>
        <td class="num">977</td>
        <td class="num">19334</td>
        <td>yes</td>
        <td class="num">1</td>
        <td class="num">1</td>
        <td class="num">1</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td><a href="issue_drafts/UD_Alemannic-DIVITAL.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="n/a" data-todo="0">
        <td><a href="treebanks/UD_Beja-Autogramm.html">Beja Autogramm</a></td>
        <td>only spoken</td>
        <td class="num">763</td>
        <td class="num">11948</td>
        <td>n/a</td>
        <td class="num">2</td>
        <td class="num">0</td>
        <td class="num">4</td>
        <td class="num">2</td>
        <td class="num">0</td>
        <td><a href="issue_drafts/UD_Beja-Autogramm.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="n/a" data-todo="0">
        <td><a href="treebanks/UD_Bokota-ChibErgIS.html">Bokota ChibErgIS</a></td>
        <td>only spoken</td>
        <td class="num">406</td>
        <td class="num">2713</td>
        <td>n/a</td>
        <td class="num">2</td>
        <td class="num">0</td>
        <td class="num">3</td>
        <td class="num">2</td>
        <td class="num">0</td>
        <td><a href="issue_drafts/UD_Bokota-ChibErgIS.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="2">
        <td><a href="treebanks/UD_Bororo-BDT.html">Bororo BDT</a></td>
        <td>mixed</td>
        <td class="num">21384</td>
        <td class="num">160356</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">2</td>
        <td><a href="issue_drafts/UD_Bororo-BDT.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="n/a" data-todo="0">
        <td><a href="treebanks/UD_Cantonese-HK.html">Cantonese HK</a></td>
        <td>only spoken</td>
        <td class="num">1004</td>
        <td class="num">13918</td>
        <td>n/a</td>
        <td class="num">2</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td><a href="issue_drafts/UD_Cantonese-HK.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="not assessed" data-todo="0">
        <td><a href="treebanks/UD_Central_Romani-Selice.html">Central_Romani Selice</a></td>
        <td>only spoken</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td>&mdash;</td>
      </tr>
      <tr data-type="only spoken" data-ident="n/a" data-todo="0">
        <td><a href="treebanks/UD_Chinese-HK.html">Chinese HK</a></td>
        <td>only spoken</td>
        <td class="num">1004</td>
        <td class="num">9874</td>
        <td>n/a</td>
        <td class="num">2</td>
        <td class="num">1</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td><a href="issue_drafts/UD_Chinese-HK.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="n/a" data-todo="0">
        <td><a href="treebanks/UD_Chukchi-HSE.html">Chukchi HSE</a></td>
        <td>only spoken</td>
        <td class="num">1004</td>
        <td class="num">5389</td>
        <td>n/a</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">5</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td><a href="issue_drafts/UD_Chukchi-HSE.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="0">
        <td><a href="treebanks/UD_Classical_Nahuatl-FloCo.html">Classical_Nahuatl FloCo</a></td>
        <td>mixed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td>&mdash;</td>
      </tr>
      <tr data-type="mixed" data-ident="yes" data-todo="0">
        <td><a href="treebanks/UD_Czech-PDTC.html">Czech PDTC</a></td>
        <td>mixed</td>
        <td class="num">213897</td>
        <td class="num">3432078</td>
        <td>yes</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td><a href="issue_drafts/UD_Czech-PDTC.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="no" data-todo="0">
        <td><a href="treebanks/UD_Danish-DDT.html">Danish DDT</a></td>
        <td>mixed</td>
        <td class="num">5512</td>
        <td class="num">100733</td>
        <td>no</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td><a href="issue_drafts/UD_Danish-DDT.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="not assessed" data-todo="0">
        <td><a href="treebanks/UD_Dargwa-Mehweb.html">Dargwa Mehweb</a></td>
        <td>only spoken</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td>&mdash;</td>
      </tr>
      <tr data-type="only spoken" data-ident="n/a" data-todo="0">
        <td><a href="treebanks/UD_English-CHILDES.html">English CHILDES</a></td>
        <td>only spoken</td>
        <td class="num">48183</td>
        <td class="num">289817</td>
        <td>n/a</td>
        <td class="num">1</td>
        <td class="num">4</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td><a href="issue_drafts/UD_English-CHILDES.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="n/a" data-todo="0">
        <td><a href="treebanks/UD_English-ESLSpok.html">English ESLSpok</a></td>
        <td>only spoken</td>
        <td class="num">2320</td>
        <td class="num">21312</td>
        <td>n/a</td>
        <td class="num">1</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td><a href="issue_drafts/UD_English-ESLSpok.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="5">
        <td><a href="treebanks/UD_English-GENTLE.html">English GENTLE</a></td>
        <td>mixed</td>
        <td class="num">1334</td>
        <td class="num">17619</td>
        <td>not assessed</td>
        <td class="num">2</td>
        <td class="num">1</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">5</td>
        <td><a href="issue_drafts/UD_English-GENTLE.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="6">
        <td><a href="treebanks/UD_English-GUM.html">English GUM</a></td>
        <td>mixed</td>
        <td class="num">14353</td>
        <td class="num">252284</td>
        <td>not assessed</td>
        <td class="num">2</td>
        <td class="num">1</td>
        <td class="num">2</td>
        <td class="num">0</td>
        <td class="num">6</td>
        <td><a href="issue_drafts/UD_English-GUM.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="7">
        <td><a href="treebanks/UD_French-ParisStories.html">French ParisStories</a></td>
        <td>only spoken</td>
        <td class="num">2776</td>
        <td class="num">42257</td>
        <td>yes</td>
        <td class="num">1</td>
        <td class="num">1</td>
        <td class="num">2</td>
        <td class="num">3</td>
        <td class="num">7</td>
        <td><a href="issue_drafts/UD_French-ParisStories.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="7">
        <td><a href="treebanks/UD_French-Rhapsodie.html">French Rhapsodie</a></td>
        <td>only spoken</td>
        <td class="num">3209</td>
        <td class="num">43691</td>
        <td>yes</td>
        <td class="num">1</td>
        <td class="num">1</td>
        <td class="num">2</td>
        <td class="num">3</td>
        <td class="num">7</td>
        <td><a href="issue_drafts/UD_French-Rhapsodie.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="3">
        <td><a href="treebanks/UD_Frisian_Dutch-Fame.html">Frisian_Dutch Fame</a></td>
        <td>only spoken</td>
        <td class="num">400</td>
        <td class="num">3729</td>
        <td>yes</td>
        <td class="num">1</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td class="num">3</td>
        <td><a href="issue_drafts/UD_Frisian_Dutch-Fame.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="1">
        <td><a href="treebanks/UD_Gheg-GPS.html">Gheg GPS</a></td>
        <td>only spoken</td>
        <td class="num">966</td>
        <td class="num">15990</td>
        <td>yes</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td class="num">1</td>
        <td><a href="issue_drafts/UD_Gheg-GPS.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="2">
        <td><a href="treebanks/UD_Greek-GDT.html">Greek GDT</a></td>
        <td>mixed</td>
        <td class="num">2521</td>
        <td class="num">61773</td>
        <td>not assessed</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">2</td>
        <td><a href="issue_drafts/UD_Greek-GDT.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="4">
        <td><a href="treebanks/UD_Greek-Lesbian.html">Greek Lesbian</a></td>
        <td>mixed</td>
        <td class="num">625</td>
        <td class="num">6624</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">3</td>
        <td class="num">0</td>
        <td class="num">4</td>
        <td><a href="issue_drafts/UD_Greek-Lesbian.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="6">
        <td><a href="treebanks/UD_Hausa-NorthernAutogramm.html">Hausa NorthernAutogramm</a></td>
        <td>only spoken</td>
        <td class="num">1305</td>
        <td class="num">15324</td>
        <td>yes</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">2</td>
        <td class="num">3</td>
        <td class="num">6</td>
        <td><a href="issue_drafts/UD_Hausa-NorthernAutogramm.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="6">
        <td><a href="treebanks/UD_Hausa-SouthernAutogramm.html">Hausa SouthernAutogramm</a></td>
        <td>only spoken</td>
        <td class="num">1927</td>
        <td class="num">14398</td>
        <td>yes</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">2</td>
        <td class="num">3</td>
        <td class="num">6</td>
        <td><a href="issue_drafts/UD_Hausa-SouthernAutogramm.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="6">
        <td><a href="treebanks/UD_Hausa-WesternAutogramm.html">Hausa WesternAutogramm</a></td>
        <td>mixed</td>
        <td class="num">775</td>
        <td class="num">13862</td>
        <td>not assessed</td>
        <td class="num">1</td>
        <td class="num">1</td>
        <td class="num">3</td>
        <td class="num">0</td>
        <td class="num">6</td>
        <td><a href="issue_drafts/UD_Hausa-WesternAutogramm.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="3">
        <td><a href="treebanks/UD_Hebrew-IAHLTknesset.html">Hebrew IAHLTknesset</a></td>
        <td>mixed</td>
        <td class="num">2883</td>
        <td class="num">50499</td>
        <td>not assessed</td>
        <td class="num">1</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">3</td>
        <td><a href="issue_drafts/UD_Hebrew-IAHLTknesset.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="7">
        <td><a href="treebanks/UD_Highland_Puebla_Nahuatl-ITML.html">Highland_Puebla_Nahuatl ITML</a></td>
        <td>mixed</td>
        <td class="num">1260</td>
        <td class="num">10018</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">5</td>
        <td class="num">0</td>
        <td class="num">7</td>
        <td><a href="issue_drafts/UD_Highland_Puebla_Nahuatl-ITML.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="4">
        <td><a href="treebanks/UD_Ika-ChibErgIS.html">Ika ChibErgIS</a></td>
        <td>only spoken</td>
        <td class="num">628</td>
        <td class="num">5307</td>
        <td>yes</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td class="num">2</td>
        <td class="num">4</td>
        <td><a href="issue_drafts/UD_Ika-ChibErgIS.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="4">
        <td><a href="treebanks/UD_Italian-KIParlaForest.html">Italian KIParlaForest</a></td>
        <td>only spoken</td>
        <td class="num">2221</td>
        <td class="num">18050</td>
        <td>yes</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td class="num">2</td>
        <td class="num">4</td>
        <td><a href="issue_drafts/UD_Italian-KIParlaForest.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="0">
        <td><a href="treebanks/UD_Japanese-JDD.html">Japanese JDD</a></td>
        <td>only spoken</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td>yes</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td>&mdash;</td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="5">
        <td><a href="treebanks/UD_Khoekhoe-KDT.html">Khoekhoe KDT</a></td>
        <td>mixed</td>
        <td class="num">3589</td>
        <td class="num">27611</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">2</td>
        <td class="num">2</td>
        <td class="num">5</td>
        <td><a href="issue_drafts/UD_Khoekhoe-KDT.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="1">
        <td><a href="treebanks/UD_Khunsari-AHA.html">Khunsari AHA</a></td>
        <td>mixed</td>
        <td class="num">10</td>
        <td class="num">74</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td>&mdash;</td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="5">
        <td><a href="treebanks/UD_Komi_Zyrian-IKDP.html">Komi_Zyrian IKDP</a></td>
        <td>only spoken</td>
        <td class="num">214</td>
        <td class="num">2304</td>
        <td>yes</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">3</td>
        <td class="num">2</td>
        <td class="num">5</td>
        <td><a href="issue_drafts/UD_Komi_Zyrian-IKDP.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="1">
        <td><a href="treebanks/UD_Latvian-LVTB.html">Latvian LVTB</a></td>
        <td>mixed</td>
        <td class="num">19580</td>
        <td class="num">330318</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td>&mdash;</td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="2">
        <td><a href="treebanks/UD_Ligurian-GLT.html">Ligurian GLT</a></td>
        <td>mixed</td>
        <td class="num">316</td>
        <td class="num">6568</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">2</td>
        <td><a href="issue_drafts/UD_Ligurian-GLT.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="6">
        <td><a href="treebanks/UD_Naija-NSC.html">Naija NSC</a></td>
        <td>only spoken</td>
        <td class="num">9241</td>
        <td class="num">140837</td>
        <td>yes</td>
        <td class="num">1</td>
        <td class="num">1</td>
        <td class="num">1</td>
        <td class="num">3</td>
        <td class="num">6</td>
        <td><a href="issue_drafts/UD_Naija-NSC.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="1">
        <td><a href="treebanks/UD_Nayini-AHA.html">Nayini AHA</a></td>
        <td>mixed</td>
        <td class="num">10</td>
        <td class="num">78</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td>&mdash;</td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="10">
        <td><a href="treebanks/UD_Nenets-Tundra.html">Nenets Tundra</a></td>
        <td>only spoken</td>
        <td class="num">170</td>
        <td class="num">1272</td>
        <td>yes</td>
        <td class="num">3</td>
        <td class="num">2</td>
        <td class="num">3</td>
        <td class="num">2</td>
        <td class="num">10</td>
        <td><a href="issue_drafts/UD_Nenets-Tundra.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="132">
        <td><a href="treebanks/UD_Nheengatu-CompLin.html">Nheengatu CompLin</a></td>
        <td>mixed</td>
        <td class="num">2839</td>
        <td class="num">26444</td>
        <td>not assessed</td>
        <td class="num">1</td>
        <td class="num">20</td>
        <td class="num">109</td>
        <td class="num">1</td>
        <td class="num">132</td>
        <td><a href="issue_drafts/UD_Nheengatu-CompLin.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="4">
        <td><a href="treebanks/UD_Northwest_Gbaya-Autogramm.html">Northwest_Gbaya Autogramm</a></td>
        <td>only spoken</td>
        <td class="num">403</td>
        <td class="num">2692</td>
        <td>yes</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td class="num">2</td>
        <td class="num">4</td>
        <td><a href="issue_drafts/UD_Northwest_Gbaya-Autogramm.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="1">
        <td><a href="treebanks/UD_Norwegian-NynorskLIA.html">Norwegian NynorskLIA</a></td>
        <td>only spoken</td>
        <td class="num">5250</td>
        <td class="num">55410</td>
        <td>yes</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td><a href="issue_drafts/UD_Norwegian-NynorskLIA.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="3">
        <td><a href="treebanks/UD_Persian-Seraji.html">Persian Seraji</a></td>
        <td>mixed</td>
        <td class="num">5997</td>
        <td class="num">151627</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">2</td>
        <td class="num">0</td>
        <td class="num">3</td>
        <td><a href="issue_drafts/UD_Persian-Seraji.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="10">
        <td><a href="treebanks/UD_Pesh-ChibErgIS.html">Pesh ChibErgIS</a></td>
        <td>only spoken</td>
        <td class="num">524</td>
        <td class="num">4275</td>
        <td>yes</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">7</td>
        <td class="num">2</td>
        <td class="num">10</td>
        <td><a href="issue_drafts/UD_Pesh-ChibErgIS.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="3">
        <td><a href="treebanks/UD_Polish-LFG.html">Polish LFG</a></td>
        <td>mixed</td>
        <td class="num">17246</td>
        <td class="num">130967</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">2</td>
        <td class="num">0</td>
        <td class="num">3</td>
        <td><a href="issue_drafts/UD_Polish-LFG.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="5">
        <td><a href="treebanks/UD_Scottish_Gaelic-ARCOSG.html">Scottish_Gaelic ARCOSG</a></td>
        <td>mixed</td>
        <td class="num">4748</td>
        <td class="num">86139</td>
        <td>not assessed</td>
        <td class="num">1</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">2</td>
        <td class="num">5</td>
        <td><a href="issue_drafts/UD_Scottish_Gaelic-ARCOSG.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="9">
        <td><a href="treebanks/UD_Skolt_Sami-Giellagas.html">Skolt_Sami Giellagas</a></td>
        <td>mixed</td>
        <td class="num">261</td>
        <td class="num">3049</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">8</td>
        <td class="num">0</td>
        <td class="num">9</td>
        <td><a href="issue_drafts/UD_Skolt_Sami-Giellagas.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="10">
        <td><a href="treebanks/UD_Slovenian-SST.html">Slovenian SST</a></td>
        <td>only spoken</td>
        <td class="num">6121</td>
        <td class="num">98393</td>
        <td>yes</td>
        <td class="num">2</td>
        <td class="num">6</td>
        <td class="num">2</td>
        <td class="num">0</td>
        <td class="num">10</td>
        <td><a href="issue_drafts/UD_Slovenian-SST.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="1">
        <td><a href="treebanks/UD_Soi-AHA.html">Soi AHA</a></td>
        <td>mixed</td>
        <td class="num">8</td>
        <td class="num">55</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td>&mdash;</td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="1">
        <td><a href="treebanks/UD_South_Levantine_Arabic-MADAR.html">South_Levantine_Arabic MADAR</a></td>
        <td>mixed</td>
        <td class="num">100</td>
        <td class="num">789</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td>&mdash;</td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="5">
        <td><a href="treebanks/UD_Spanish-COSER.html">Spanish COSER</a></td>
        <td>only spoken</td>
        <td class="num">539</td>
        <td class="num">7987</td>
        <td>yes</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">5</td>
        <td class="num">0</td>
        <td class="num">5</td>
        <td><a href="issue_drafts/UD_Spanish-COSER.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="0">
        <td><a href="treebanks/UD_Swedish_Sign_Language-SSLC.html">Swedish_Sign_Language SSLC</a></td>
        <td>only spoken</td>
        <td class="num">203</td>
        <td class="num">1610</td>
        <td>yes</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td>&mdash;</td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="1">
        <td><a href="treebanks/UD_Telugu_English-TECT.html">Telugu_English TECT</a></td>
        <td>only spoken</td>
        <td class="num">97</td>
        <td class="num">456</td>
        <td>yes</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td class="num">1</td>
        <td><a href="issue_drafts/UD_Telugu_English-TECT.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="4">
        <td><a href="treebanks/UD_Turkish_English-BUTR.html">Turkish_English BUTR</a></td>
        <td>only spoken</td>
        <td class="num">58</td>
        <td class="num">441</td>
        <td>yes</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">3</td>
        <td class="num">1</td>
        <td class="num">4</td>
        <td><a href="issue_drafts/UD_Turkish_English-BUTR.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="3">
        <td><a href="treebanks/UD_Turkish_German-SAGT.html">Turkish_German SAGT</a></td>
        <td>only spoken</td>
        <td class="num">2184</td>
        <td class="num">36934</td>
        <td>yes</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">2</td>
        <td class="num">1</td>
        <td class="num">3</td>
        <td><a href="issue_drafts/UD_Turkish_German-SAGT.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="5">
        <td><a href="treebanks/UD_Ukrainian-ParlaMint.html">Ukrainian ParlaMint</a></td>
        <td>mixed</td>
        <td class="num">7142</td>
        <td class="num">109166</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">3</td>
        <td class="num">1</td>
        <td class="num">5</td>
        <td><a href="issue_drafts/UD_Ukrainian-ParlaMint.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="2">
        <td><a href="treebanks/UD_Vietnamese-TueCL.html">Vietnamese TueCL</a></td>
        <td>only spoken</td>
        <td class="num">100</td>
        <td class="num">1888</td>
        <td>yes</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">2</td>
        <td class="num">0</td>
        <td class="num">2</td>
        <td><a href="issue_drafts/UD_Vietnamese-TueCL.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="3">
        <td><a href="treebanks/UD_Western_Armenian-ArmTDP.html">Western_Armenian ArmTDP</a></td>
        <td>mixed</td>
        <td class="num">6644</td>
        <td class="num">121432</td>
        <td>not assessed</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">3</td>
        <td><a href="issue_drafts/UD_Western_Armenian-ArmTDP.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="18">
        <td><a href="treebanks/UD_Western_Sierra_Puebla_Nahuatl-MesoTree.html">Western_Sierra_Puebla_Nahuatl MesoTree</a></td>
        <td>mixed</td>
        <td class="num">3024</td>
        <td class="num">19191</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">4</td>
        <td class="num">13</td>
        <td class="num">0</td>
        <td class="num">18</td>
        <td><a href="issue_drafts/UD_Western_Sierra_Puebla_Nahuatl-MesoTree.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="mixed" data-ident="not assessed" data-todo="6">
        <td><a href="treebanks/UD_Yiddish-YiTB.html">Yiddish YiTB</a></td>
        <td>mixed</td>
        <td class="num">3113</td>
        <td class="num">27954</td>
        <td>not assessed</td>
        <td class="num">0</td>
        <td class="num">2</td>
        <td class="num">3</td>
        <td class="num">0</td>
        <td class="num">6</td>
        <td><a href="issue_drafts/UD_Yiddish-YiTB.html">draft &#8599;</a></td>
      </tr>
      <tr data-type="only spoken" data-ident="yes" data-todo="1">
        <td><a href="treebanks/UD_Zazaki-ZSD.html">Zazaki ZSD</a></td>
        <td>only spoken</td>
        <td class="num">200</td>
        <td class="num">1371</td>
        <td>yes</td>
        <td class="num">0</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td class="num">0</td>
        <td class="num">1</td>
        <td><a href="issue_drafts/UD_Zazaki-ZSD.html">draft &#8599;</a></td>
      </tr>
  </tbody>
</table>

<style>
#tb-controls { display: flex; flex-wrap: wrap; gap: 0.6rem; align-items: center; margin: 1rem 0; }
#tb-controls input[type="text"] { padding: 0.3rem 0.5rem; min-width: 220px; }
#tb-controls select { padding: 0.3rem 0.4rem; }
#tb-count { margin-left: auto; font-size: 0.9em; color: #666; }
#tb-table { border-collapse: collapse; width: 100%; }
#tb-table th, #tb-table td { border: 1px solid #ccc; padding: 4px 8px; text-align: left; font-size: 0.92em; }
#tb-table td.num, #tb-table th[data-type="number"] { text-align: right; }
#tb-table th { background: #f0f0f0; cursor: pointer; user-select: none; white-space: nowrap; }
#tb-table th:hover { background: #e2e2e2; }
#tb-table th.sorted-asc::after { content: " \25B2"; }
#tb-table th.sorted-desc::after { content: " \25BC"; }
#tb-table tr.tb-hidden { display: none; }
</style>

<script>
(function () {
  var table = document.getElementById('tb-table');
  var tbody = table.querySelector('tbody');
  var rows = Array.prototype.slice.call(tbody.querySelectorAll('tr'));
  var searchBox = document.getElementById('tb-search');
  var typeFilter = document.getElementById('tb-type-filter');
  var identFilter = document.getElementById('tb-ident-filter');
  var todoOnly = document.getElementById('tb-todo-only');
  var countEl = document.getElementById('tb-count');

  function applyFilters() {
    var q = searchBox.value.trim().toLowerCase();
    var t = typeFilter.value;
    var ident = identFilter.value;
    var onlyTodo = todoOnly.checked;
    var visible = 0;
    rows.forEach(function (row) {
      var name = row.cells[0].textContent.toLowerCase();
      var matchesSearch = !q || name.indexOf(q) !== -1;
      var matchesType = !t || row.getAttribute('data-type') === t;
      var matchesIdent = !ident || row.getAttribute('data-ident') === ident;
      var matchesTodo = !onlyTodo || parseInt(row.getAttribute('data-todo'), 10) > 0;
      var show = matchesSearch && matchesType && matchesIdent && matchesTodo;
      row.classList.toggle('tb-hidden', !show);
      if (show) visible++;
    });
    countEl.textContent = visible + ' / ' + rows.length + ' treebanks shown';
  }

  searchBox.addEventListener('input', applyFilters);
  typeFilter.addEventListener('change', applyFilters);
  identFilter.addEventListener('change', applyFilters);
  todoOnly.addEventListener('change', applyFilters);

  var sortState = { col: null, dir: 1 };
  table.querySelectorAll('th').forEach(function (th) {
    th.addEventListener('click', function () {
      var col = parseInt(th.getAttribute('data-col'), 10);
      var type = th.getAttribute('data-type');
      var dir = (sortState.col === col) ? -sortState.dir : 1;
      sortState = { col: col, dir: dir };

      table.querySelectorAll('th').forEach(function (h) { h.classList.remove('sorted-asc', 'sorted-desc'); });
      th.classList.add(dir === 1 ? 'sorted-asc' : 'sorted-desc');

      rows.sort(function (a, b) {
        var va = a.cells[col].textContent.trim();
        var vb = b.cells[col].textContent.trim();
        if (type === 'number') {
          return (parseFloat(va) - parseFloat(vb)) * dir;
        }
        return va.localeCompare(vb) * dir;
      });
      rows.forEach(function (row) { tbody.appendChild(row); });
    });
  });

  applyFilters();
})();
</script>

## Harmonization Pipeline:

1. is spoken part clearly identifiable?
   1. `yes` > add `# modality = spoken` to relevant sentences
   2. `no` > open ISSUE with text XXXX

## Workflow
- Per-treebank data (all reviewed fields, per-field advice, and a manual-check list) lives in `workgroups/spoken-data/treebanks/<Treebank>.md` - one file per treebank.
- This index is a generated recap; edit the per-treebank files, not this table, then regenerate.
- Per-treebank issue drafts summarizing needed changes are available in `workgroups/spoken-data/issue_drafts/` and linked from the "issue draft" column above.
- I hope I didn't get anything wrong. -L
