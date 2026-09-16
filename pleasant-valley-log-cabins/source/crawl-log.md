# Crawl log

NOTE: during the crawl, a stray `<a href="file:///C:/PVLC Web Files/cabrental.html">`
link found on the two gallery pages (Bird's Nest / Bear's Den — a leftover local-disk
link from the original author's FrontPage PC, not a real pvlc.com URL) was
mis-resolved by the crawler to `http://www.pvlc.com/file:///C:/PVLC%20Web%20Files/cabrental.html`,
which 404'd and briefly overwrote the good `html/cabrental.html` (both requests wrote to
the same local filename `cabrental.html`). This was caught during review and
`html/cabrental.html` was re-fetched directly from `http://www.pvlc.com/cabrental.html`
(HTTP 200, 11485 bytes, verified correct content) after the crawl finished. Final
`html/cabrental.html` on disk is the good 11485-byte version, not the 404 page.

Three full-size photos (Deer meadow outside front.jpg, bearsdenfront1.jpg,
Birds nest frontview.jpg, Moose Lodge side view.JPG) were reached only via `<a href>`
(linked full-size original behind a thumbnail `<img>`), so the crawler script initially
saved them into html/ instead of images/ — manually moved into images/ post-crawl,
and duplicate copies removed from html/. Final locations for every real image are
under source/images/.

- PAGE http://www.pvlc.com/index.html -> html/index.html (HTTP 200, 11701 bytes)
- PAGE http://www.pvlc.com/cabrental.html -> html/cabrental.html (HTTP 200, 11485 bytes) [re-fetched after crawl; see note above]
- PAGE http://www.pvlc.com/cabinfacilities.html -> html/cabinfacilities.html (HTTP 200, 7803 bytes)
- PAGE http://www.pvlc.com/CabinRentalRates.html -> html/CabinRentalRates.html (HTTP 200, 27938 bytes)
- PAGE http://www.pvlc.com/localmap.html -> html/localmap.html (HTTP 200, 2840 bytes)
- PAGE http://www.pvlc.com/Ski%20Package%20Special.htm -> html/Ski Package Special.htm (HTTP 200, 11611 bytes)
- PAGE http://www.pvlc.com/Our%20Family.html -> html/Our Family.html (HTTP 200, 1209 bytes)
- PAGE http://www.pvlc.com/winter_at_pleasant_valley.html -> html/winter_at_pleasant_valley.html (HTTP 200, 5490 bytes)
- PAGE http://www.pvlc.com/photo%20gallery%20Moose%20Lodge.html -> html/photo gallery Moose Lodge.html (HTTP 200, 2949 bytes)
- PAGE http://www.pvlc.com/photo%20gallery%20dear%20meadow%20cabin.html -> html/photo gallery dear meadow cabin.html (HTTP 200, 2220 bytes)
- PAGE http://www.pvlc.com/photo_gallery_for_the_bird.html -> html/photo_gallery_for_the_bird.html (HTTP 200, 1966 bytes)
- PAGE http://www.pvlc.com/photo_gallery_for_the_bears_den.html -> html/photo_gallery_for_the_bears_den.html (HTTP 200, 2254 bytes)
- PAGE http://www.pvlc.com/Moose_Lodge_Front_View.JPG -> html/Moose_Lodge_Front_View.JPG (HTTP 200, 509518 bytes)
- PAGE http://www.pvlc.com/Deer%20meadow%20outside%20front.jpg -> html/Deer meadow outside front.jpg (HTTP 200, 271440 bytes)
- PAGE http://www.pvlc.com/Birds%20nest%20sideview.jpg -> html/Birds nest sideview.jpg (HTTP 200, 304287 bytes)
- PAGE http://www.pvlc.com/bearsdenfront1.jpg -> html/bearsdenfront1.jpg (HTTP 200, 592008 bytes)
- PAGE http://www.pvlc.com/Moose%20Lodge%20side%20view.JPG -> html/Moose Lodge side view.JPG (HTTP 200, 561476 bytes)
- PAGE http://www.pvlc.com/lg%20cabin%20front.jpg -> html/lg cabin front.jpg (HTTP 200, 99792 bytes)
- PAGE http://www.pvlc.com/photo%20gallery%20large%20cabin.html -> html/photo gallery large cabin.html (HTTP 200, 2234 bytes)
- PAGE http://www.pvlc.com/Birds%20nest%20frontview.jpg -> html/Birds nest frontview.jpg (HTTP 200, 350542 bytes)
- PAGE http://www.pvlc.com/pleasant_valley_is_a_winter_wond.html -> html/pleasant_valley_is_a_winter_wond.html (HTTP 200, 1672 bytes)
- PAGE http://www.pvlc.com/file:///C:/PVLC%20Web%20Files/cabrental.html -> html/cabrental.html (HTTP 404, 355 bytes)

# Images
- IMG http://www.pvlc.com/Birds%20nest%20sideview.jpg -> images/Birds nest sideview.jpg (HTTP 200, 304287 bytes)
- IMG http://www.pvlc.com/Birds_nest_frontview_small.jpg -> images/Birds_nest_frontview_small.jpg (HTTP 200, 2211 bytes)
- IMG http://www.pvlc.com/Birds_nest_sideview_small.jpg -> images/Birds_nest_sideview_small.jpg (HTTP 200, 2345 bytes)
- IMG http://www.pvlc.com/Deer_meadow_outside_front_small.jpg -> images/Deer_meadow_outside_front_small.jpg (HTTP 200, 1872 bytes)
- IMG http://www.pvlc.com/Family%20pic%20with%20horses%202016.jpg -> images/Family pic with horses 2016.jpg (HTTP 200, 185959 bytes)
- IMG http://www.pvlc.com/Fisher106.jpg -> images/Fisher106.jpg (HTTP 200, 220781 bytes)
- IMG http://www.pvlc.com/Fisher109.jpg -> images/Fisher109.jpg (HTTP 200, 258055 bytes)
- IMG http://www.pvlc.com/Fisher111.jpg -> images/Fisher111.jpg (HTTP 200, 139404 bytes)
- IMG http://www.pvlc.com/Fisher116.jpg -> images/Fisher116.jpg (HTTP 200, 193178 bytes)
- IMG http://www.pvlc.com/Large%20map%20to%20Pleasant%20Valley.png -> images/Large map to Pleasant Valley.png (HTTP 200, 525521 bytes)
- IMG http://www.pvlc.com/Moose_Lodge_Front_View.JPG -> images/Moose_Lodge_Front_View.JPG (HTTP 200, 509518 bytes)
- IMG http://www.pvlc.com/Moose_Lodge_Front_View_small.JPG -> images/Moose_Lodge_Front_View_small.JPG (HTTP 200, 2069 bytes)
- IMG http://www.pvlc.com/Moose_Lodge_side_view.JPG -> images/Moose_Lodge_side_view.JPG (HTTP 200, 540842 bytes)
- IMG http://www.pvlc.com/Moose_Lodge_side_view_small.JPG -> images/Moose_Lodge_side_view_small.JPG (HTTP 200, 2196 bytes)
- IMG http://www.pvlc.com/Ski%20Package%20Photo.jpg -> images/Ski Package Photo.jpg (HTTP 200, 113821 bytes)
- IMG http://www.pvlc.com/Small%20map%20to%20Pleasant%20Valley.png -> images/Small map to Pleasant Valley.png (HTTP 200, 46733 bytes)
- IMG http://www.pvlc.com/animate.js -> images/animate.js (HTTP 200, 14261 bytes)
- IMG http://www.pvlc.com/bearsdenaboveview.jpg -> images/bearsdenaboveview.jpg (HTTP 200, 859820 bytes)
- IMG http://www.pvlc.com/bearsdenbathroom.jpg -> images/bearsdenbathroom.jpg (HTTP 200, 823160 bytes)
- IMG http://www.pvlc.com/bearsdenbathtub.jpg -> images/bearsdenbathtub.jpg (HTTP 200, 853904 bytes)
- IMG http://www.pvlc.com/bearsdenfront1_small.jpg -> images/bearsdenfront1_small.jpg (HTTP 200, 3258 bytes)
- IMG http://www.pvlc.com/bearsdenfront1_small1.jpg -> images/bearsdenfront1_small1.jpg (HTTP 200, 3258 bytes)
- IMG http://www.pvlc.com/bearsdenfront2.jpg -> images/bearsdenfront2.jpg (HTTP 200, 622004 bytes)
- IMG http://www.pvlc.com/bearsdenfrontporchview.jpg -> images/bearsdenfrontporchview.jpg (HTTP 200, 846859 bytes)
- IMG http://www.pvlc.com/bearsdenkitchen.jpg -> images/bearsdenkitchen.jpg (HTTP 200, 858851 bytes)
- IMG http://www.pvlc.com/bearsdenloftview.jpg -> images/bearsdenloftview.jpg (HTTP 200, 867954 bytes)
- IMG http://www.pvlc.com/bearsdenskywalkview.jpg -> images/bearsdenskywalkview.jpg (HTTP 200, 861313 bytes)
- IMG http://www.pvlc.com/bicycle_318-101809.jpg -> images/bicycle_318-101809.jpg (HTTP 200, 5947 bytes)
- IMG http://www.pvlc.com/button11.gif -> images/button11.gif (HTTP 200, 652 bytes)
- IMG http://www.pvlc.com/button26.gif -> images/button26.gif (HTTP 200, 579 bytes)
- IMG http://www.pvlc.com/hiking_318-29056.jpg -> images/hiking_318-29056.jpg (HTTP 200, 25711 bytes)
- IMG http://www.pvlc.com/hummingbird_318-107119.jpg -> images/hummingbird_318-107119.jpg (HTTP 200, 3594 bytes)
- IMG http://www.pvlc.com/kayak_318-115903.jpg -> images/kayak_318-115903.jpg (HTTP 200, 5842 bytes)
- IMG http://www.pvlc.com/lg%20cabin%20front.jpg -> images/lg cabin front.jpg (HTTP 200, 99792 bytes)
- IMG http://www.pvlc.com/lg%20cabin%20inside.jpg -> images/lg cabin inside.jpg (HTTP 200, 41696 bytes)
- IMG http://www.pvlc.com/lg%20cabin%20porch.jpg -> images/lg cabin porch.jpg (HTTP 200, 83744 bytes)
- IMG http://www.pvlc.com/lg%20cabin%20side.jpg -> images/lg cabin side.jpg (HTTP 200, 84142 bytes)
- IMG http://www.pvlc.com/lg_cabin_front_small.jpg -> images/lg_cabin_front_small.jpg (HTTP 200, 2449 bytes)
- IMG http://www.pvlc.com/moose%20lodge%20bedroom.JPG -> images/moose lodge bedroom.JPG (HTTP 200, 140712 bytes)
- IMG http://www.pvlc.com/moose%20lodge%20downstairs.JPG -> images/moose lodge downstairs.JPG (HTTP 200, 186167 bytes)
- IMG http://www.pvlc.com/moose%20lodge%20kitchen.JPG -> images/moose lodge kitchen.JPG (HTTP 200, 159017 bytes)
- IMG http://www.pvlc.com/moose%20lodge%20porch%20view%201.JPG -> images/moose lodge porch view 1.JPG (HTTP 200, 290868 bytes)
- IMG http://www.pvlc.com/moose%20lodge%20upstairs%20bath.JPG -> images/moose lodge upstairs bath.JPG (HTTP 200, 170457 bytes)
- IMG http://www.pvlc.com/silhouette-of-a-man-riding-a-horse_318-27519.jpg -> images/silhouette-of-a-man-riding-a-horse_318-27519.jpg (HTTP 200, 24409 bytes)
- IMG http://www.pvlc.com/ski-stick-man_318-83719.jpg -> images/ski-stick-man_318-83719.jpg (HTTP 200, 5225 bytes)
- IMG http://www.pvlc.com/swimming-student-on-sports-class_318-58787.jpg -> images/swimming-student-on-sports-class_318-58787.jpg (HTTP 200, 36642 bytes)
- IMG http://www.pvlc.com/winter%20cabin%20pic.jpg -> images/winter cabin pic.jpg (HTTP 200, 40704 bytes)
- IMG http://www.pvlc.com/winter%20cabin%20pic3.jpg -> images/winter cabin pic3.jpg (HTTP 200, 219748 bytes)
- IMG http://www.pvlc.com/winter%20sign%20pic.jpg -> images/winter sign pic.jpg (HTTP 200, 156137 bytes)
