// @flow
import React from 'react'
import {Bio, BioGroup} from 'components'
//import BioGroup from "./BioGroup";

type Props = {}

const ContactUsView = () => (
        <div>
            <BioGroup header={"Professional Staff"}>
                <Bio name={"Brett Hunt"} position={"Executive Director"} email={"brett.hunt@asu.edu"} pictureURL={"https://media.licdn.com/media/p/6/005/06f/10d/37f07f4.jpg"}/>
                <Bio name={"Jessica Eldridge"} position={"Assistant Director"} email={"jessica.eldridge@asu.edu"} pictureURL={"https://media.licdn.com/media/p/2/000/2b4/161/38a250d.jpg"}/>
                <Bio name={"Laura Tan"} position={"Community Engagement Coordinator"} email={"laura.tan@asu.edu"} pictureURL={"https://media.licdn.com/media/p/6/005/09c/2ca/2e7e1f7.jpg"}/>
                <Bio name={"Veronica Gutierrez"} position={"Curriculum and Course Manager"} email={"veronica.gutierrez@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t31.0-8/26678217_10109089048805231_1239174116842371196_o.jpg?oh=d353c7b96da89b13b54e5cf4791f8bc0&oe=5B09F765"}/>
            </BioGroup>

            <BioGroup header={"Chief of Staff and Leads"}>
                <Bio name={"Eric Arellano"} position={"Chief of Staff"} email={"eric.arellano@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/26815372_1505477482841281_4162892782714660624_n.jpg?oh=1d246da8e20a909b20410066bdb65d4a&oe=5B10E643"}/>
                <Bio name={"Michelle Thomas"} position={"Culture Lead"} email={"mthoma38@asu.edu"} pictureURL={"https://media.licdn.com/media/AAIA_wDGAAAAAQAAAAAAAAmlAAAAJGFhOTg2MzVhLTVmMTAtNDcyNC1hNGU1LTIxMzkwOTEzZjNkOA.jpg"}/>
                <Bio name={"Kelly Bitler"} position={"Education Lead"} email={"kelly.bitler@asu.edu"} pictureURL={"https://media.licdn.com/media/AAEAAQAAAAAAAAcvAAAAJDA3NDIwZWFlLTc5ODMtNGUyMy1hNTlmLTFhMDkzMzViM2IyMA.jpg"}/>
                <Bio name={"Steven Sawtelle"} position={"Engagement Lead"} email={"steven.sawtelle@asu.edu"} pictureURL={"https://media.licdn.com/media/AAEAAQAAAAAAAAjNAAAAJDExZmY0YTcxLWU1ODAtNDVjMi1hZmRkLTUyNTZhOTZmZDFhZQ.jpg"}/>
            </BioGroup>

            <BioGroup header={"Committee Chairs"}>
                <Bio name={"Diana Chen"} position={"Admin"} email={"dkchen1@asu.edu"} pictureURL={"https://media.licdn.com/media/AAEAAQAAAAAAAAPmAAAAJDE2YWU4NThmLTkyNGYtNDg4NC04MzQyLWFlZTljMDk4ZGQ4Nw.jpg"}/>
                <Bio name={"Henry Hoang"} position={"Ambassadors"} email={"henry.hoang@asu.edu"} pictureURL={"https://media.licdn.com/media/AAIA_wDGAAAAAQAAAAAAAAqmAAAAJGZiMGU4NzJlLTE4MTktNDkzYy04ZGM2LWVhNDhlMDcxMDYxNw.jpg"}/>
                <Bio name={"Matthew Moy"} position={"Civil-Mil"} email={"matthew.moy@asu.edu"} pictureURL={"https://media.licdn.com/media/AAMABADGAAwAAQAAAAAAABHxAAAAJDcwNGRmNjMyLTEwNjctNDYxYy04MDYzLTQ5ZGJmMGRlMWI3Mg.jpg"}/>
                <Bio name={"Anna Piper"} position={"Communications"} email={"aepiper@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/25592090_10213446410226713_5324301000887542779_n.jpg?oh=7c6a7bf8641365ec8255a970aadcb865&oe=5B179CF0"}/>
                <Bio name={"David Huff"} position={"Events"} email={"david.r.huff@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/24993450_1202445663222249_5173404211670915679_n.jpg?oh=c93352a8342a2ab947679bd03a6eb5b4&oe=5B16F9B5"}/>
                <Bio name={"Zechariah Wilson"} position={"Mentoring"} email={"zechariah.wilson@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t31.0-8/18320748_1075707785896268_8301408790625505922_o.jpg?oh=04802d0b560b48b70b9c901cd224fa79&oe=5B0FAE95"}/>
                <Bio name={"Courtney Langerud"} position={"Service"} email={"courtney.langerud@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/25353791_1574152102679880_3886755589891247003_n.jpg?oh=a355728f293fd955894d3e89f9e153ea&oe=5ADE90EA"}/>
                <Bio name={"Kara Lehmann"} position={"Social"} email={"kara.lehmann@asu.edu"} pictureURL={"https://media.licdn.com/media/AAEAAQAAAAAAAAebAAAAJGJhMTNmOTQ5LWYwM2YtNGU4NC1iZDE0LTNkZmQ4MmVhZDk3MA.jpg"}/>
                <Bio name={"Adam Thompson"} position={"Training"} email={"adam.richard.thompson@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/27750841_1452239774905278_109012201486380910_n.jpg?oh=3d4239d32c9776c1627cb9a634b996de&oe=5B2637CD"}/>
            </BioGroup>

            <BioGroup header={"Section Leaders"}>
                <Bio name={"Keri Orcutt"} position={"Section 1"} email={"klorcutt@asu.edu"} pictureURL={"https://media.licdn.com/media/AAIA_wDGAAAAAQAAAAAAAAx9AAAAJGM0MWFkMWZjLWUzM2ItNGEyOC04ZDNlLTYxYzNiMWM5MDJhNA.jpg"}/>
                <Bio name={"Lerman Montoya"} position={"Section 2"} email={"lerman.montoya@asu.edu"} pictureURL={"https://media.licdn.com/media/AAIABADGAAAAAQAAAAAAAAvTAAAAJDM1MjQ1YmMxLTExMjktNDAzNS1hZDQ4LTUwNTEzMDJmMzc5Nw.jpg"}/>
                <Bio name={"Jacob Anderson"} position={"Section 3"} email={"jacob.michael.anderson@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/1010532_572000982894705_761319501_n.jpg?oh=519a59ac9517f30432adc92805f1f8b4&oe=5B156F03"}/>
                <Bio name={"Cayla Roy"} position={"Section 4"} email={"cayla.roy@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/21369258_1557458437608168_6040908416369055684_n.jpg?oh=60c55cca3f22917629862a8c13d0cfba&oe=5B00B30C"}/>
                <Bio name={"Kelly Walsh"} position={"Section 5"} email={"kewalsh@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/28168137_1924087197619212_9059379090590928983_n.jpg?oh=6b68d043baff5affcf9ebd34c2fdc8fc&oe=5B4CDBDA"}/>
                <Bio name={"Lauren Barnes"} position={"Section 6"} email={"labarne4@asu.edu"} pictureURL={"https://media.licdn.com/media/AAIABADGAAAAAQAAAAAAAAsZAAAAJDAzMzE4MGFkLTJkZGUtNDIwZi1hMDQwLWVmN2ZiZjBjOGFkOA.jpg"}/>
                <Bio name={"Arianna Kurtz"} position={"Section 7"} email={"arianna.kurtz@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-1/c0.78.320.320/p320x320/26165782_1528798800546371_6954385807188231029_n.jpg?oh=41964eed2237a048febc47a3d19fa0e1&oe=5B1DA3FA"}/>
                <Bio name={"Markanday Ravi"} position={"Section 8"} email={"mravi2@asu.edu"} pictureURL={"https://media.licdn.com/media/AAEAAQAAAAAAAAleAAAAJDViNzlhY2E2LWY0MTUtNDI4Mi1iZDQ5LTg2MjIwNzFmYTBkYw.jpg"}/>
                <Bio name={"Raquel Torres"} position={"Section 9"} email={"rtorres3830@gmail.com"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t31.0-8/25626362_1646213235435383_3142513556461247602_o.jpg?oh=4982117ddde7453e54b2a1b85ef6b4cf&oe=5B0A5530"}/>
                <Bio name={"Anirudh Koka"} position={"Section 10"} email={"anirudh.koka@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/15541968_1414311528580940_3796488980490883980_n.jpg?oh=f65560e7d60824f85baccb056714b87e&oe=5B072A60"}/>
            </BioGroup>

            <BioGroup header={"Mission Team Leaders 1-15"}>
                <Bio name={"Annaleez Fishkind"} position={"MT1: Sexual and Domestic Violence"} email={"annaleez.fishkind@asu.edu"} pictureURL={"https://pbs.twimg.com/profile_images/877314427720052736/zXNXEr3B.jpg"}/>
                <Bio name={"Brianna Feller"} position={"MT2: Human Trafficking"} email={"bnfeller@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/20664725_474565929572849_6561836422131053239_n.jpg?oh=a45f9259a24577579143d723f99f2907&oe=5B1D5700"}/>
                <Bio name={"Haley Nadone"} position={"MT3: Gender Equality"} email={"haley.nadone@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/21761565_359066077864712_7187104374056896778_n.jpg?oh=772cccd99a1c9caf6307988e694feb98&oe=5B085409"}/>
                <Bio name={"McKenna Byrne"} position={"MT4: Racial & LGBTQ Equality"} email={"mckenna.byrne@asu.edu"} pictureURL={"https://media.licdn.com/media/AAEAAQAAAAAAAAhuAAAAJGU2MjIyYmEwLTgzNDktNDA0Zi04MDE4LTRiMDc1ZmJhOTI5OQ.jpg"}/>
                <Bio name={"Ellen Lam"} position={"MT5: Immigration"} email={"ellen.lam@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/15747864_1560195917340418_1271783088227207924_n.jpg?oh=111e40af35ca58c00dfea77d00aa0adf&oe=5B100A01"}/>
                <Bio name={"Abigail Walker"} position={"MT6: Cultural & Global Equality"} email={"abigail.m.walker@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/17904182_1329665590447654_3030165610206481774_n.jpg?oh=a80dc71be0a65d3a68574dcd9ab3cf0d&oe=5B0D21FF"}/>
                <Bio name={"Britton Jones"} position={"MT7: Justice"} email={"britton.jones@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/12651114_132666753783045_5799098087211508946_n.jpg?oh=170ba652a7da5994ce95faf70f13b6d2&oe=5B07FC3E"}/>
                <Bio name={"Jake Baker"} position={"MT8: Justice"} email={"jake.baker.1@asu.edu"} pictureURL={"https://media.licdn.com/media/AAEAAQAAAAAAAAx2AAAAJDMwOGFjYjA2LTY5M2QtNDYyYS1hNDBiLTM3MTc1NTFmMzM5OQ.jpg"}/>
                <Bio name={"Miguel Montanez"} position={"MT9: Homelessness"} email={"miguel.montanez@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/13043607_1144563332305216_7805747488942075802_n.jpg?oh=98f9e80bd7499278c66a582858614009&oe=5B0902FB"}/>
                <Bio name={"Kirsten Spencer"} position={"MT10: Youth Development"} email={"kirsten.spencher@asu.edu"} pictureURL={"https://pbs.twimg.com/profile_images/877314427720052736/zXNXEr3B.jpg"}/>
                <Bio name={"Emma Sounart"} position={"MT11: Disabilities & Empowerment"} email={"emma.sounart@asu.edu"} pictureURL={"https://media.licdn.com/media/AAMABADGAAwAAQAAAAAAAAxzAAAAJDMzYjJkYWZjLThmNTgtNDM0My05ZGJiLTFhNWU1MzU0ZDhjYw.jpg"}/>
                <Bio name={"Katja Klosterman"} position={"MT12: Healthcare Access"} email={"katja.klosterman@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/21687608_276439699512702_8691988110552036578_n.jpg?oh=6bea4577eb3a93cfa77cc3fc501c9009&oe=5B0563F1"}/>
                <Bio name={"Devan Pratt"} position={"MT13: Security"} email={"dcpratt1@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/10438898_742395732556370_329130413867763347_n.jpg?oh=67f5ae5ec8eb1e1b6599b67d58a051be&oe=5B11C18D"}/>
                <Bio name={"Michael Redmond"} position={"MT14: Community Development"} email={"michael.redmond@asu.edu"} pictureURL={"https://media.licdn.com/media/AAMAAQDuAAgAAQAAAAAAABDPAAAAJGE3ZTZkZjkzLTZkYzYtNGFkNi05NjEwLTE5NzViZTdhM2YzZg.bin"}/>
                <Bio name={"Jordan Paul"} position={"MT15: Security"} email={"jtpaul20@hotmail.com"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/19657283_1413556345397037_2967285048553981257_n.jpg?oh=160501d7b1e20531f6f73f5b59ba5b66&oe=5B08FDD0"}/>
            </BioGroup>

            <BioGroup header={"Mission Team Leaders 16-30"}>
                <Bio name={"Brandon Lew"} position={"MT16: Veterans Healthcare & Services"} email={"brandon.lew@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/13260105_1596568617320969_7353826535503585327_n.jpg?oh=6883fb0c523dff03d54ad932b92b7ab6&oe=5B1CBBCD"}/>
                <Bio name={"Emily Brzezinski"} position={"MT17: Mental Health"} email={"ebrzezi1@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/21317675_1443225589091892_6832156261208190840_n.jpg?oh=3180ebe8b418a9d7795190954e81e516&oe=5B08F71B"}/>
                <Bio name={"Dominique Player"} position={"MT18: Mental Health"} email={"dvplayer@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/27657171_10155071330356160_3174511979431011649_n.jpg?oh=57e144f6118e815477b190a1a4e34f0e&oe=5B015518"}/>
                <Bio name={"Claudia Luna"} position={"MT19: Public Health"} email={"cluna11@asu.edu"} pictureURL={"https://instagram.fphx1-1.fna.fbcdn.net/vp/a3ba9a52e630b883c17de9ea349e1896/5B0DB102/t51.2885-19/s150x150/27580567_152807045432722_6795003540650590208_n.jpg"}/>
                <Bio name={"Victoria Alonso"} position={"MT20: Healthcare Access"} email={"victoria.i.alonso@asu.edu"} pictureURL={"https://pbs.twimg.com/profile_images/877314427720052736/zXNXEr3B.jpg"}/>
                <Bio name={"Haley Rivard-Lentz"} position={"MT21: Hunger & Nutrition"} email={"haley.rivard-lentz@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/26730713_1188024497998108_1819083280807086663_n.jpg?oh=59e0b5236977454369370cf49e721a98&oe=5B1D89A6"}/>
                <Bio name={"Hailey Campbell"} position={"MT22: Environmental Sustainability"} email={"hailey.campbell@asu.edu"} pictureURL={"https://media.licdn.com/media/AAIA_wDGAAAAAQAAAAAAAAojAAAAJDM0Yjg5NGMwLWU5NTgtNGVjNC1iMDdlLTYyOTMxZDUxMjQ2Mg.jpg"}/>
                <Bio name={"Kathryn Harris"} position={"MT23: Sustainability"} email={"kathryn.j.harris@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/11224362_1037093356356352_3275845753120358040_n.jpg?oh=71d7467884e112437bb467cdcfd10cf9&oe=5B0E1DF0"}/>
                <Bio name={"Julie Pham"} position={"MT24: Energy & Climate Sustainability"} email={"juliepham@gmail.com"} pictureURL={"https://media.licdn.com/media/AAEAAQAAAAAAAArJAAAAJDYyMjA2ZTBmLWQwM2UtNDg4Ny04MGExLTQ0ZWQ1NDAyZWY2MQ.jpg"}/>
                <Bio name={"Casey Blue"} position={"MT25: Sustainability"} email={"casey.blue@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/27971875_364141777386489_6382860131233502331_n.jpg?oh=a55555d32d9a329cb3701732b356e36e&oe=5B06CE96"}/>
                <Bio name={"Brett Goldsmith"} position={"MT26: Water Access & Sustainability"} email={"brett.goldsmith@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/16508830_869749203128810_4642246434102943763_n.jpg?oh=dac6587752af5aa7390b0068d353c4c6&oe=5B081B6B"}/>
                <Bio name={"William Atkin"} position={"MT27: Energy & Climate Sustainability"} email={"william.atkin@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/13418962_1023816641029122_4755008855237312740_n.jpg?oh=9d834a115b7a1155eb9e5d19717332dc&oe=5B4DF98B"}/>
                <Bio name={"Matthew Stockmal"} position={"MT28: Education & Policy"} email={"matthew.stockmal@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/16508830_869749203128810_4642246434102943763_n.jpg?oh=dac6587752af5aa7390b0068d353c4c6&oe=5B081B6B"}/>
                <Bio name={"Madison Arnold"} position={"MT29: Education"} email={"madison.arnold.1@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/15107444_1612269835454493_2333612002911913476_n.jpg?oh=baee08be51bc1f7c16b732a535cd5018&oe=5B18F5B9"}/>
                <Bio name={"Richa Venkatraman"} position={"MT30: Education"} email={"rvenka25@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/22366641_819390111555039_1003135440516017389_n.jpg?oh=e4e3cc787731c5fca243743824d38a28&oe=5B1F9B66"}/>
            </BioGroup>
        </div>
    )

export default ContactUsView