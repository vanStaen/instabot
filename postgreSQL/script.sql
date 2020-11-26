/* Update Active bool and iterations 
UPDATE public.config_accounts_insta
	SET active=?, iterations=?, tags=?, username=?
	WHERE <condition>; */

UPDATE public.config_accounts_insta
	SET active='True', iterations='30'
	WHERE username='miralykkeofficial';

UPDATE public.config_accounts_insta
	SET active='True', iterations='50'
	WHERE username='vanstaenmusic';

UPDATE public.config_accounts_insta
    SET active='True', iterations='50'
	WHERE username='tt.lykke';

UPDATE public.config_accounts_insta
	SET active='True', iterations='50'
	WHERE username='clementvanstaen';

UPDATE public.config_accounts_insta
	SET active='True', iterations='50'
	WHERE username='theresapogge';

UPDATE public.config_accounts_insta
	SET active='True', iterations='50'
	WHERE username='deuxfrancs';

UPDATE public.config_accounts_insta
	SET active='True', iterations='60'
	WHERE username='dukevonstein';

UPDATE public.config_accounts_insta
	SET active='True', iterations='30'
	WHERE username='purzelbaumrecords';


/* Update Tags */
UPDATE public.config_accounts_insta
	SET tags= ARRAY [ 'bdsmcommunity','losangeles']
	WHERE username='dukevonstein';
