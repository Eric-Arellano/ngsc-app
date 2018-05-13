// @flow

import type { Name } from 'types'
import jacobRagsdale from './photos/jacob-ragsdale.jpg'

export type BioType = {
  name: Name,
  position: string,
  email: string,
  pictureURL: string,
}

export type BioGroupType = {
  group: string,
  bios: Array<BioType>,
}

export const bioGroupsData: Array<BioGroupType> = [
  {
    group: 'Professional Staff',
    bios: [
      {
        name: {
          first: 'Brett',
          last: 'Hunt'
        },
        position: 'Executive Director',
        email: 'brett.hunt@asu.edu',
        pictureURL: 'https://media.licdn.com/dms/image/C4E03AQEZhdBD_g71lw/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=PtxvyFt752cYRK8T5-_UBt0Zm0OmAwwuIqTmRszARpw'
      },
      {
        name: {
          first: 'Jessica',
          last: 'Eldridge'
        },
        position: 'Assistant Director',
        email: 'jessica.eldridge@asu.edu',
        pictureURL: 'https://media.licdn.com/dms/image/C5603AQFZodEmhbZklg/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=2RTWz6XPLTfkwe8JJboA8QhJkWUKZaAGzLXqgjfpqDY'
      },
      {
        name: {
          first: 'Laura',
          last: 'Tan'
        },
        position: 'Community Engagement Coordinator',
        email: 'laura.tan@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/295423_262292843879255_1708700154_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeFW7Njp6Oo410Y3OccOqDLNPjTK6XWuxt0xsVggoxoC1jEtRoEe8uHFowAMrhYlIRXuGFg14lu8gsjd094xw5hoATCtVvoJvgIbh6VprVr53g&oh=ecb8929f3e4202b2ad8dbef7017cb21b&oe=5B344FA3'
      },
      {
        name: {
          first: 'Veronica',
          last: 'Gutierrez'
        },
        position: 'Curriculum and Course Manager',
        email: 'veronica.gutierrez@asu.edu',
        pictureURL: 'https://scontent.fphx1-1.fna.fbcdn.net/v/t31.0-8/26678217_10109089048805231_1239174116842371196_o.jpg?oh=d353c7b96da89b13b54e5cf4791f8bc0&oe=5B09F765'
      }
    ]
  },
  {
    group: 'Chief of Staff and Committee Leads',
    bios: [
      {
        name: {
          first: 'Kara',
          last: 'Lehmann'
        },
        position: 'Chief of Staff',
        email: 'Kara.Lehmann@asu.edu',
        pictureURL: 'https://media.licdn.com/dms/image/C5103AQEg_3HmNMpWaQ/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=N8xvwwupgSVbciIHWMoS_lpSeHaWmpNuU1kLnTycdO4'
      },
      {
        name: {
          first: 'David',
          last: 'Huff'
        },
        position: 'Culture Lead',
        email: 'David.R.Huff@asu.edu',
        pictureURL: 'https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/24993450_1202445663222249_5173404211670915679_n.jpg?oh=c93352a8342a2ab947679bd03a6eb5b4&oe=5B16F9B5'
      },
      {
        name: {
          first: 'Adam',
          last: 'Thompson'
        },
        position: 'Education Lead',
        email: 'Adam.Richard.Thompson@asu.edu',
        pictureURL: 'https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/27750841_1452239774905278_109012201486380910_n.jpg?oh=3d4239d32c9776c1627cb9a634b996de&oe=5B2637CD'
      },
      {
        name: {
          first: 'Matthew',
          last: 'Moy'
        },
        position: 'Engagement Lead',
        email: 'Matthew.Moy@asu.edu',
        pictureURL: 'https://media.licdn.com/dms/image/C5603AQG9-vhumjBmdw/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=6pvItHDToctRCuVc5BTvfiUBQRCXrEZiAXAlv8ePk7Q'
      },
    ]
  },
  {
    group: 'Section Leads',
    bios: [
      {
        name: {
          first: 'Savanna',
          last: 'Soldevere'
        },
        position: 'Section 1',
        email: 'ssoldeve@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/28795721_1675923255835460_7141392406632362971_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeEpjJ1OfO0bPf1i8mPyTzO0zrGLksLYVwrdmGfdfyt1XGUVmEULbXYNme-_m5hxwqfikPDV80s93qexPWBugBkYbAvT2LBKge6KzuwC3v6J-A&oh=aa50a19681781a152842821af20f0d37&oe=5B65CE2B'
      },
      {
        name: {
          first: 'Truc',
          last: 'Doan'
        },
        position: 'Section 2',
        email: 'tldoan@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t31.0-8/25073085_10208142107589059_8061053466842241584_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGbOe7zKtxBjpoocbyfKhSTZwOuzBcp0ptHVEeHm5_tLBCdwlaT3rAgFTIkFXPr27cnYGHzmL--VNrop-Z1qge3HWP3TAkCfbkOFXi5wheAGg&oh=15edd1bdc7cd4cf3d659526f1826e5d7&oe=5B6C30A2'
      },
      {
        name: {
          first: 'Jordan',
          last: 'Paul'
        },
        position: 'Section 3',
        email: 'jtpaul1@asu.edu',
        pictureURL: 'https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/19657283_1413556345397037_2967285048553981257_n.jpg?oh=160501d7b1e20531f6f73f5b59ba5b66&oe=5B08FDD0'
      },
      {
        name: {
          first: 'Emma',
          last: 'Sounart'
        },
        position: 'Section 4',
        email: 'Emma.Sounart@asu.edu',
        pictureURL: 'https://media.licdn.com/dms/image/C5603AQHdyVxgfrh7UA/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=EPwks-Vy0I2gKo5Oj7prZVA8hK-aTkU0tiB8zhpsm-k'
      },
      {
        name: {
          first: 'Katja',
          last: 'Klosterman'
        },
        position: 'Section 5',
        email: 'Katja.Klosterman@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t31.0-8/21640745_276439699512702_8691988110552036578_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeG2u-3dt7A_az0O4gzTci7_nv6XF4HLhKybkgSzNDStx_-ARdDo4zZ-0_AYukrfv63q-iED0htUUQ2wc-FoooBiIOfUN04EntwLXmvymJpe7A&oh=cab16e617938a50dc1d82bc7faf8376b&oe=5B304F30'
      },
      {
        name: {
          first: 'Marianna',
          last: 'Peña'
        },
        position: 'Section 6',
        email: 'Mariana.Pena@asu.edu',
        pictureURL: 'https://media.licdn.com/dms/image/C4D03AQEgu8rLnSkEQg/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=LzzqiO7P_L30ZaCSzrUlWmetay7BaEN_cDmG6DXKGGk'
      },
      {
        name: {
          first: 'Andrea',
          last: 'Arellano'
        },
        position: 'Section 7',
        email: 'Andrea.Arellano.1@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/29792700_1086979038111957_2769352569781246734_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeHbCd1O3Zbon-S0SR5_k7ORTR8W38MMXhIPFhxqrYQgDFSZNP52sfLYBQizNW04w5EZuWpaaNbutGv1nZr51hCxoEO-1uRYbxQlZK61mDkQjA&oh=0c3b699e4e1a4955e7b1851d0544dd07&oe=5B664505'
      },
      {
        name: {
          first: 'Jacob',
          last: 'Ragsdale'
        },
        position: 'Section 8',
        email: 'Jacob.Ragsdale@asu.edu',
        pictureURL: jacobRagsdale
      },
      {
        name: {
          first: 'Samantha',
          last: 'Stone'
        },
        position: 'Section 9',
        email: 'Samantha.F.Stone@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/15747557_1292463974147727_4193737941078067186_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeHuFCpm6PPhiFIHVACNZQOnskr0AqDu4aGdwZSgE-Gp9g8QGQYy87axZB9qRQiSgcBj53edQQDetGFYZsx8-Ov7xdKgo24Cx1vacnrYLZ7eYA&oh=96578ee475e8cce4f8053e6f2444cdc8&oe=5B35DDC2'
      },
      {
        name: {
          first: 'Maddie',
          last: 'Arnold'
        },
        position: 'Section 10',
        email: 'madison.arnold.1@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/15107444_1612269835454493_2333612002911913476_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGKfLEXIMpd0Bbu0C41rdDBCy4yp3SXdMX5cdwl5podXBNCXlm6F2rA1fpvaefiQm22R7CLJsFBBhal1WBbS8WSACWRtiXYjFNrppfxX9Mgiw&oh=25ee0fe9fc8d8d1a80cb573f962a5f86&oe=5B680FB9'
      },
    ]
  },
  {
    group: 'Committee Chairs',
    bios: [
      {
        name: {
          first: 'Jeremy',
          last: 'Seidner'
        },
        position: 'Admin Chair',
        email: 'jseidne@asu.edu',
        pictureURL: 'https://media.licdn.com/dms/image/C5603AQGledn5coGyVw/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=xVjDZW-qa651bieLyMI5R5NYJWuJjlgExQA_yKcTSJQ'
      },
      {
        name: {
          first: 'Drew',
          last: 'Hackmann'
        },
        position: 'Ambassadors Chair',
        email: 'ehackma1@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/16831977_1867537380189704_7874044308575759814_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeH3NySFx2GnOeXTEmZHlTe9QWa7mgPvvKm_yTFH7A33rpuTIpOaADc5YeeTVzzjv009bQa6TCTWOB3LQVy-i90DhekS-OWBpOpjsh-Z40dCyQ&oh=d2d33a9df39049d2a545e5785a568149&oe=5B2A395A'
      },
      {
        name: {
          first: 'Breanna',
          last: 'Wright'
        },
        position: 'Civil-Mil Chair',
        email: 'brwrigh1@asu.edu',
        pictureURL: 'https://media.licdn.com/dms/image/C5603AQG1Q0pMozaYcg/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=ntZBsTmCahfu_khTskVx_3AtXvgkmca_JpUj64z1lhE'
      },
      {
        name: {
          first: 'Sara',
          last: 'Neves Perez'
        },
        position: 'Communications Chair',
        email: 'Sara.Nevespereira@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/19060026_10212235284504635_4234299516823943275_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeFZV6sCWBusApiI7pYoAyILFL9YB-k4lrnaaLjiBw4YaJ1twcrQI1_VgOaM3Jnnz780BFGnn30F3uFHQVjZ1aM48Z3UB-ST9raAWhDcEPEwcA&oh=aa57ec0ef4a06373ea8686aed3bcdfc1&oe=5B362EC1'
      },
      {
        name: {
          first: 'Justin',
          last: 'Rainge'
        },
        position: 'Events Chair',
        email: 'jrainge@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t31.0-8/21768940_1929571243934485_8974410512505753576_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGWc0OZESLyWlxwbSesk9kVFomqzfekfHxKpFOJkuvH0N9sI6uXaApNyLesXH4TEVhwrC_eGg77HTQvZ2g33OAEPoYU3BJN-qoHjPo21HGnZg&oh=dadc032135d729fd1475b04326a55af1&oe=5B299651'
      },
      {
        name: {
          first: 'Caroline',
          last: 'Livingston'
        },
        position: 'Mentorship Chair',
        email: 'cslivin1@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t31.0-8/17880148_780493898782379_5991580927269278218_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGSx3jRrLqDOdtDw4vyyMxn_uadYF74I-iKRetqs2M-OYkod8Tv-eGPr2GGsMfZYNihqtbIEcmoEQkVLUaxaMJswAAcTWeskB-SsZMcK2cPqA&oh=a2cda67d900b5dab071ee1fddb4a2d22&oe=5B73DCB9'
      },
      {
        name: {
          first: 'Katherine',
          last: 'Niche'
        },
        position: 'Service Chair',
        email: 'kniche@asu.edu',
        pictureURL: 'https://scontent.fsnc1-1.fna.fbcdn.net/v/t1.0-9/18198194_1302564229857843_8425745054606263217_n.jpg?_nc_cat=0&oh=ae7b7e30f133a2a4827a188a0cfd3635&oe=5B981E05'
      },
      {
        name: {
          first: 'Tayelee',
          last: 'Holtrop'
        },
        position: 'Social Chair',
        email: 'tholtrop@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/23473282_153980968547040_560708824949638159_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeG3aCa3v_11Gemuk9Gy3MA7qQiJAZaXVsasP2fupR2wfvLv_RPKEiU-4yUVJJS8EkL29z3lW7bItTIz5ByORld-vDpfFDxEclQ_IJ3l1yo1jQ&oh=edbe3bfa83c1893c9b821c61f5604581&oe=5B75F4AB'
      },
      {
        name: {
          first: 'Joey',
          last: 'Graham'
        },
        position: 'Training Chair',
        email: 'jmgrah10@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/10624643_732878030092678_8120086573989626366_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGZr19m9hvv4TcXNg7R0WArFEthIKHfFwUqP9EFzle4trqvskGvrGn9JJKR5YJEP67zNu4W9eJZXzOXEaR9MMJKj1D7lpWW5XFCwmmFkJNo8A&oh=356b2aa4a51c06208dd3f38d5fd69f1f&oe=5B358479'
      },
      {
        name: {
          first: 'Kyla',
          last: 'Christenson'
        },
        position: 'Transfer Chair',
        email: 'Kyla.Christenson@asu.edu',
        pictureURL: 'https://media.licdn.com/dms/image/C4D03AQGJivSPiznj2w/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=H_Ab3BCNHtLUsKyuWSboth4wlwK6P4wlWsCsDe01hMs'
      },
    ]
  },
  {
    group: 'Mission Teams',
    bios: [
      {
        name: {
          first: 'Shea',
          last: 'Brutinel',
        },
        position: 'MT 1 - Sexual & Domestic Violence',
        email: 'sbrutine@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/21369197_1478258892266196_4499690090165972590_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeE_cp8rkiJah868dw8phg6UfruLfaTVZx2XoihNJMjuOSE8iB--9EzsmkaBCxlQGyEwqDB8HEhrUznZB44he0SnK6MleqDxtLBhSMOalAy7Xw&oh=5563ba32f39d42c99e8b7a634ed247a0&oe=5B711F22',
      },
      {
        name: {
          first: 'Jessica',
          last: 'Francis',
        },
        position: 'MT 2 - Human Trafficking',
        email: 'jfranc24@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/27336700_1498191083612983_1956229876721712277_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeHN3AatMKFgVaNyU6Qxht045HhpSFPL7rusbEblpIsor9OBQCeI47MKBjOzFhnwr2c6O4mvvFx0VT0hQlTcrUIu9GwBRzWV7Jd7HdhwuEcrCQ&oh=b10cb80ca77b9e0988e72fd49e13e260&oe=5B27CE51',
      },
      {
        name: {
          first: 'Jane',
          last: 'Halfhill',
        },
        position: 'MT 3 - Gender Equality',
        email: 'jlhalfhi@asu.edu',
        pictureURL: 'https://scontent-lax3-2.xx.fbcdn.net/v/t1.0-9/19884255_1044670422334359_202157560100418868_n.jpg?_nc_cat=0&oh=92da284b4539591a02097cc79cfa084d&oe=5B588428',
      },
      {
        name: {
          first: 'Marisa',
          last: 'Eldridge',
        },
        position: 'MT 4 - Racial & LGBTQ Equality',
        email: 'mneldrid@asu.edu',
        pictureURL: 'https://media.licdn.com/dms/image/C4D03AQFLs6i-c753eQ/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=UZqjxvDyip0CaiUWEftClJ3teE7AfRaZxJK3IwiwDow',
      },
      {
        name: {
          first: 'Raul',
          last: 'Tapia',
        },
        position: 'MT 5 - Immigration',
        email: 'Jesus.R.Tapia@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/12650904_978792422191821_3387201371454587093_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeEjQltFrkRbsru5369T_YpJlPo779oxbIpXNpiTPgW7jmGLJBdOKf9tmIv0CxvolENr2n2d91r2GgCeub1IKowH_yb_JQuFnfoIAG_HiavHeQ&oh=b6fb8ca7fd5103e2f780146bfc4d8b1c&oe=5B6E5A3C',
      },
      {
        name: {
          first: 'Jeneeshia',
          last: 'Jose',
        },
        position: 'MT 6 - Cultural & Global Equality',
        email: 'jjose5@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/18622283_1206623986113209_3109728238922392843_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeHca2LRUFKUkW7ELBPO0yweExu0oR4o7lFX-G4MnDg_V9nzbhYvGYJyLhh39iysX8uQJXFK71Tas9TIzBTsIK6vFfuavjIk228e9517JTDoTw&oh=1dfc84e75be1d5794aac6410ce8d914f&oe=5B3998F0',
      },
      {
        name: {
          first: 'Daiva',
          last: 'Scovil',
        },
        position: 'MT 7 - Criminal Justice',
        email: 'dscovil@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/18739921_2303263503231678_6076459444731137223_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGJJ0a58bzI75Bt5u0DboOONTo0GBshNier6p6lswEHAaPlhOkZr9CG5xtOTLKvnP728mAgCGar9kmisVbRoV1GWihk2SM8d7wsAm8zF8OwjA&oh=41773537911b932c12d866f7b37d84d8&oe=5B32217B',
      },
      {
        name: {
          first: 'Mary',
          last: 'Vidal',
        },
        position: 'MT 8 - Security',
        email: 'mvvidal@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/29177118_1081769055309666_1460970650916544069_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGagTIBgs6EDNcZxOLUgBVnQ23DLE81zg6ULvXUHvnTItZVG6ohpg9VSoBj6niYEHMO70b1Mi60aehF5FCrNs0MySIA5eWZMoY6SqodFqLslg&oh=f122d8cd065e9f910ff52f8b1ed49798&oe=5B6D75F2',
      },
      {
        name: {
          first: 'Mia',
          last: 'Sablan',
        },
        position: 'MT 9 - Community Development',
        email: 'mpsablan@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/26993980_105084330306328_5112471371682069571_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeH9hdMOX7uPq57SObK24NWeH0HY5rdjzk4sKGixl9iyJVT74kB-pGHdLUBZ0R5XGpYGLQr_E04Ss47_YJMyVitRTVOaHGQ6w4GesQvrw382Lg&oh=2ac030f79d2f12dee46b9ee185caca22&oe=5B6D5603',
      },
      {
        name: {
          first: 'Taylor',
          last: 'Carstens',
        },
        position: 'MT 10 - Youth Development',
        email: 'tlcarste@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/29244277_1476497145811026_2708219644564471808_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeEjCNvSOuKlglG9gZi2e_IP-Gilc6jAGrTCiBITR1J0IEeScGHQXiYygs37UQt2xldTgAMxSlvxHeqUFql5Li30drq47F_wIat5oX4YE0jc5Q&oh=669a39ed91c2fcc8283023489d0411f4&oe=5B270017',
      },
      {
        name: {
          first: 'Alana',
          last: 'Ramirez',
        },
        position: 'MT 11 - Civic Engagement',
        email: 'aramir96@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/29136354_2070045446339712_9050133057796833280_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeFalOcaJOTIbIANNWtv_259OgIKZwrx8fjqLRCPk1HIq0EjI5E9eJTjOWHPc5w6l-zsB58pczaGJvOqNeTa0x3r9Cqwhdwp9HzNnNqZY8VSaA&oh=8fe9ba9beb8c8292b945f214eb02ea98&oe=5B684620',
      },
      {
        name: {
          first: 'Hunter',
          last: 'Allen',
        },
        position: 'MT 12 - Disabilities & Empowerment',
        email: 'haallen2@asu.edu',
        pictureURL: 'https://scontent-lax3-2.xx.fbcdn.net/v/t1.0-9/27867825_1731411606905427_298820547642512337_n.jpg?_nc_cat=0&oh=8c2d69e1c91e48e11d0e9d7620e75163&oe=5B5D7255',
      },
      {
        name: {
          first: 'Ray',
          last: 'Regorgo',
        },
        position: 'MT 13 - Access to Healthcare',
        email: 'rlregorg@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/23172399_1977253352492841_5094224241819580112_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeF3iGdroTuP4pmQ0awMr20JDCdcnT_roSMTkL5kARJwiZlUUwOXnah3cVleMRe8NTO15VPn5jjpYiRPqKlVkySMYHQ2m7kvQ6QWrEQ1N52PWA&oh=bdd4249d84234d42415a7d0b9ce21663&oe=5B68ECF0',
      },
      {
        name: {
          first: 'Riley',
          last: 'O\'Toole',
        },
        position: 'MT 14 - Access to Healthcare',
        email: 'rmotoole@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/20429924_1591841024173232_8054839933463628297_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeHSFpT11qEJ1QLZizrEPbuVB7mQ2_WSDnEUPZ63kSm4ofSIVAcXsmyd5FNAqyhBLV2tAMWFCaSOw5KOjT8giif5awIyhruwkXOLEghvTzIchw&oh=d3c0a4922e7e85be7a82a3bcb44d4b53&oe=5B68A1AC',
      },
      {
        name: {
          first: 'Chance',
          last: 'Jones',
        },
        position: 'MT 15 - Veterans Healthcare & Services',
        email: 'Chance.Jones@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-1/29571370_903225509802817_525459460618179537_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeECIESnps-DBaQmR2rZ6_BHlr2ANltMwGj7xb6E27rdZZceBcrK89qTtXHIssZs3cKZEIhjKhEgA2h6efnuxj43mIU9RM96E50-ql5lf9J9dg&oh=34aa8812197c71e21997db0808c1b244&oe=5B338B9B',
      },
      {
        name: {
          first: 'Josh',
          last: 'Kumar',
        },
        position: 'MT 16 - Public Health',
        email: 'Joshua.M.Kumar@asu.edu',
        pictureURL: 'https://media.licdn.com/dms/image/C4E03AQH6BUlTIi7AAA/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=RLTPsCTHHbeSTMmdccNJTscpV3IizNKLaCpnBnY-COU',
      },
      {
        name: {
          first: 'Mady',
          last: 'Privatsky',
        },
        position: 'MT 17 - Mental Health',
        email: 'mprivats@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/27972737_1035662576574609_8412136046921582079_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeFrUDIZge7lYDKP4TA3ITuZH1vhxEiI1kk4Grs-kyRF4smR9Kcwx5Wegh0gV88RS2K_qdvSbjuEyMTz-ZkIFDVtwmU3ZgP7Ckoc3NvMZGfetA&oh=26ec4be8944e4eb16ab3aabe7eae725b&oe=5B68A6BF',
      },
      {
        name: {
          first: 'Elizabeth',
          last: 'Pino',
        },
        position: 'MT 18 - Mental Health',
        email: 'epino1@asu.edu',
        pictureURL: 'https://media.licdn.com/dms/image/C5603AQGV1YBTN86mNg/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=BmD-5RiDrAPYy8vM2by9YhffSzTy7eNCD9EXVMWEuo4',
      },
      {
        name: {
          first: 'Kelsey',
          last: 'Atcheson',
        },
        position: 'MT 19 - Homelessness',
        email: 'katcheso@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/21462564_301146440360641_4862088140188246245_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeF_OKaUMUF3qiKZiaXGtMuLR7Z9SVB6S_hWdCheTCQyjRgvNMN46lLSa_55i8-G-dc5pXPp632NDVUTzX1uNUnluOVPj3FMIgALeuvZFM7I1A&oh=4d91eed5e8043d9f47e39e7e4f4f1c2c&oe=5B70255D',
      },
      {
        name: {
          first: 'Mikayla',
          last: 'Beatty',
        },
        position: 'MT 20 - Science, Technology, & Innovation',
        email: 'mrbeatt1@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/27331673_161792431130658_6742593474795921291_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGZ-GfcxhSre5miERdEYmQaExE-NazHioJ4ROaBjjvQjNS88QNXjZUtCr2voc4O1OrzXxeDKzq1FcSRkkCzlfTRZ6hVPGVEPSjms8onMhoMFA&oh=f784aeb58e0f0c696bb4be333509d37a&oe=5B37FA9A',
      },
      {
        name: {
          first: 'Marisela',
          last: 'Arias',
        },
        position: 'MT 21 - Hunger & Nutrition',
        email: 'marias10@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-1/27867824_1580981285272848_3534441539306129269_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeFwWxG56zKBXPxltS8XjPuTNrdnm0eq6d7UXjbkGwq3yn1lTxbTtnfe9iNdTYxtCH168Lb0wsH22jsGXuDV9048Al3otqC1dXgYNQPLp02DSw&oh=dc494bca40ecf8fdf2a8cc17d6ddaa90&oe=5B731C24',
      },
      {
        name: {
          first: 'Consuelo',
          last: 'Arroyo',
        },
        position: 'MT 22 - Environmental Sustainability',
        email: 'carroyo3@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/15284077_1877061835858101_4177114520453946885_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGbi2iTTAa_pH1y8NEiPNKDZ7SKIEhde8YO4pH2w6TRrf4UG8mZ3K537VZfkzWU_QQ_DjACMMYD8ZYDINU7ApCrbvx0KRsDVil1W65xr0dn2w&oh=8d914bb5c70d87003f3c4cda413bd56c&oe=5B6AA593',
      },
      {
        name: {
          first: 'Jack',
          last: 'Fuller',
        },
        position: 'MT 23 - Sustainability',
        email: 'jrfulle6@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/13516411_122854414809833_2024540420430407184_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeH45TIm5XIH2j5PHnT7OAOWGJCkdMsBH6mmkLp4OQP-g_z0prPNvFDYMomytU_1jAyi0Paf49Bbo3Sa2E6j3_xCSbEafp5LTxn-rhDHrhgh_A&oh=52acfb842f85ce8f142294f547258cb9&oe=5B2FF6CA',
      },
      {
        name: {
          first: 'Rachel',
          last: 'Spencer',
        },
        position: 'MT 24 - Animal Rights',
        email: 'rmspenc2@asu.edu',
        pictureURL: 'https://scontent.fsnc1-1.fna.fbcdn.net/v/t1.0-9/25353841_1748903012072508_3414789447634174856_n.jpg?_nc_cat=0&oh=fdd7ccc25181f54523ea040eb88357b2&oe=5B98786D',
      },
      {
        name: {
          first: 'Claire',
          last: 'Block',
        },
        position: 'MT 25 - Sustainability',
        email: 'cblock3@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/14713526_649232478577895_2036347344205480931_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeFRLYaKiT26mcC1WrEIRlqnJ9UtRwdXzdtfa5YV1A-2anFFCDlqhJlHS940tj450Ttz9G-B_zYIXqr2AyaUja8nJ3_xgwE5jMdHYHzAFnV0wQ&oh=af2ca484829ad618d914ca93ec20d0a8&oe=5B6D7E0D',
      },
      {
        name: {
          first: 'Sai',
          last: 'Kottapalli',
        },
        position: 'MT 26 - Water Access & Sustainability',
        email: 'sbkottap@asu.edu',
        pictureURL: 'https://scontent-lax3-2.xx.fbcdn.net/v/t1.0-9/28870687_1971882069506554_3813903811737922659_n.jpg?_nc_cat=0&oh=1ed24ca71cceac237776523bcb2ba911&oe=5B689707',
      },
      {
        name: {
          first: 'Carlos',
          last: 'Zamora',
        },
        position: 'MT 27 - Energy & Climate Sustainability',
        email: 'cazamor1@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/21105546_115892235807478_6757796221769618757_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeHzgpViGUSKMO_A4JM6AqXZWVP923F7TP2-O3oORIIM08u8tpD0umY6d7UdmPwrzSLrD6HV6lYNQ1n9HTkL-jC425AFFZevRSccIb55d2wezw&oh=58bb6a8393cdee2f86c7e4d80f21aee4&oe=5B70A23C',
      },
      {
        name: {
          first: 'Bailey',
          last: 'De La Torre',
        },
        position: 'MT 28 - Education & Policy',
        email: 'bcdelato@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/16142381_10208135948612657_5443882619920928199_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeED_-uvC684mTpA1I9RgqqqHb9vCdk2uw9YAZj7NBYIzS5uXuxC5H7RyxU5Q7kaCY-uPpIE2QU3sO5nbqGQLtBlijllzQ7eKe4UkkgXBIqb_Q&oh=1b90575997ce1916e2aaf13a2c6307be&oe=5B270E2E',
      },
      {
        name: {
          first: 'Angel',
          last: 'Morales',
        },
        position: 'MT 29 - Education',
        email: 'acmoral4@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/22195784_497240107298788_2100061400948613900_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeFAfF8m7dK6kNihnrbNgwWjMJGh2i20mRdw3v-WEKyX9y_TJqq8tfX3FZ8R86R3sSwNLXzR-BzNVj8BQG_-zZclNHgmBI215RKpDS12-ROAxw&oh=faf6376d0a61b3604cc76ac2d7a9c1ca&oe=5B342D11',
      },
      {
        name: {
          first: 'Cyrus',
          last: 'Commissariat',
        },
        position: 'MT 30 - Education',
        email: 'ccommiss@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/29542846_349286485565852_6542615990104512195_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeHjF5-yWyPO_siEFInE9vREKeXgM_vwZ7qlVc2RTXCfG0V0b5H-6_c3MpkMS5Szu66N4OBTwkymyEK9n2lYfJC0nFLOHFs4zV7GVsge7_vPow&oh=acd1f48e46cf6bf897d339498ca64e7f&oe=5B656D66',
      },
    ]
  },
]