--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: memories; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.memories (
    id integer NOT NULL,
    image character varying(255),
    song character varying(255),
    description character varying(255),
    aromas character varying(80),
    x integer,
    y integer,
    room_id integer
);


--
-- Name: memories_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.memories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: memories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.memories_id_seq OWNED BY public.memories.id;


--
-- Name: rooms; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.rooms (
    id integer NOT NULL,
    name character varying(80) NOT NULL,
    image character varying(255),
    user_id integer
);


--
-- Name: rooms_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.rooms_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: rooms_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.rooms_id_seq OWNED BY public.rooms.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(80) NOT NULL,
    email character varying(100) NOT NULL
);


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: memories id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.memories ALTER COLUMN id SET DEFAULT nextval('public.memories_id_seq'::regclass);


--
-- Name: rooms id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rooms ALTER COLUMN id SET DEFAULT nextval('public.rooms_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: memories; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.memories (id, image, song, description, aromas, x, y, room_id) FROM stdin;
1	https://itdoesnttastelikechicken.com/wp-content/uploads/2017/05/super-moist-vegan-banana-nut-muffins-easy-dairy-free-facebook.jpg’	https://open.spotify.com/album/3mGmn1JDde3XyKQqZTJUAL?highlight=spotify:track:4QxDOjgpYtQDxxbWPuEJOy	Your mothers secret recipe for those banana nut muffins	Crisp winter air, hot cocoa, fresh baked banana bread	500	550	1
2	https://merriam-webster.com/assets/mw/images/article/art-wap-landing-mp-lg/family-of-four-7101-a234e9249b2c7223d4e4d8cd9432f9e9@1x.jpg	https://open.spotify.com/album/3alZBOvPaK3hgMEEymw4Yr?highlight=spotify:track:0mHyWYXmmCB9iQyK18m3FQ	Babysittng your grandchildren every Sunday	Baby powder, diapers, fresh peaches	209	379	1
3	https://cdn.images.express.co.uk/img/dynamic/41/590x/monopoly-gamer-board-games-reboot-super-mario-nintendo-823505.jpg	https://open.spotify.com/album/6mmv0gwumlFGWDGJXF4yEv?highlight=spotify:track:29U7stRjqHU6rMiS8BfaI9	Playing monopoly and drinking lemonade	Lemons, fresh cut roses	677	785	1
4	https://i.pinimg.com/236x/3e/81/2f/3e812f93fc028189d5b2b761e164ff6a--a-christmas-story-christmas-morning.jpg	https://open.spotify.com/track/2yPoRJvPqwpbGLJPRikrZW?si=13b08af526f24414	Christmas morning when Ralphie got the Red Rider he wanted so badly	Fresh pine, torn paper, coffee	414	346	2
5	https://static01.nyt.com/images/2016/09/12/watching/12watching1/12watching1-superJumbo-v2.jpg	https://open.spotify.com/track/3MXfueQqoiF93unHCQZos2?si=a274b3b4699741f2	Mike, Lucas, and Will playing Dungeons and Dragons while having a sleep over	Mac n cheese, stinky shoes	224	756	2
6	https://i1.wp.com/highdefdiscnews.com/wp-content/uploads/2018/10/the_great_outdoors_11.png?ssl=1	https://open.spotify.com/track/7demHL0GXA6YmTNqw3Btz8?si=1c2afaeb41a14a8b	One of the best camping trips with the family	Campfire, pine trees, old cabin	570	714	2
7	https://c1.staticflickr.com/9/8452/7984891423_309149ea12_b.jpg	https://open.spotify.com/album/77spqXa3VNN0mw13PgWWyY?highlight=spotify:track:6n6OQfBpCgzF9oEg8zhBN7	Playing with my grandkids in the backyard	Freshly mowed grass	602	831	3
8	https://wpcluster.dctdigital.com/sundaypost/wp-content/uploads/sites/13/2017/08/JE0165_royalty-free-image_family-BBQ-smartbrush_AW2_060217-1024x683.jpg	https://open.spotify.com/album/4sSXylKcBB3p47VfrBJlfK?highlight=spotify:track:1LM5zQv5pBKPyO7rm7Uz6U	Family BBQs after church on Sundays	grill smoke	530	463	3
9	https://cdn.images.dailystar.co.uk/dynamic/1/photos/551000/620x/Young-girl-flying-a-kite-682596.jpg	https://open.spotify.com/album/3usnShwygMXVZB4IV5dwnU?highlight=spotify:track:2RlgNHKcydI9sayD2Df2xp	Teaching the kids how to fly kites	Sunshine on the skin	200	831	3
10	https://amz.netweather.tv/monthly_09_2015/post-2611-0-09582700-1442308742.jpg	https://open.spotify.com/album/1CsuCA05y9r7ftG9bGGtWV?highlight=spotify:track:3m167vBQI5YLK0a1m6L6Y1	The blizzard where the whole neighborhood came together and dug out the driveway	Crisp winter air, hot cocoa, bacon and eggs for breakfast	510	422	4
11	https://flashbak.com/wp-content/uploads/2017/09/078_1967-1026x1024.jpg	https://open.spotify.com/album/6lPb7Eoon6QPbscWbMsk6a?highlight=spotify:track:4uGIJG1jYFonGc4LGp5uQL	Dancing at Lindas garden party	Fruit punch, aftershave, honeysuckle	315	647	4
12	https://groovyhistory.com/content/124227/f0e9bedffd72ead0c2b92d96674be472.jpg	https://open.spotify.com/album/5Qcef60m4gcckV24PmPYVq?highlight=spotify:track:2rUHBIfbMBB92n1gSfSqwF	Tailgating outside Madison Square Garden waiting to see Bruce Springsteen in concert	Net hairspray, beer, hot pavement	119	377	4
\.


--
-- Data for Name: rooms; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.rooms (id, name, image, user_id) FROM stdin;
1	Kitchen	https://user-images.githubusercontent.com/65255478/109369416-81cc3b80-7859-11eb-8bc6-f4647040555a.png	1
2	Living Room	https://user-images.githubusercontent.com/65255478/109369440-901a5780-7859-11eb-83e9-350d3f3494ec.png	1
3	Backyard	https://user-images.githubusercontent.com/65255478/109369423-87c21c80-7859-11eb-8559-43a0cf43e9a9.png	1
4	Bedroom	https://user-images.githubusercontent.com/65255478/109369427-8a247680-7859-11eb-9330-b282ea6b4907.png	1
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.users (id, name, email) FROM stdin;
1	iandouglas	ian.douglas@iandouglas.com
\.


--
-- Name: memories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.memories_id_seq', 12, true);


--
-- Name: rooms_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.rooms_id_seq', 4, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_id_seq', 1, true);


--
-- Name: memories memories_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.memories
    ADD CONSTRAINT memories_pkey PRIMARY KEY (id);


--
-- Name: rooms rooms_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rooms
    ADD CONSTRAINT rooms_pkey PRIMARY KEY (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: memories memories_room_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.memories
    ADD CONSTRAINT memories_room_id_fkey FOREIGN KEY (room_id) REFERENCES public.rooms(id);


--
-- Name: rooms rooms_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rooms
    ADD CONSTRAINT rooms_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

