export const actions = {
  default: async ({ request, cookies }) => {
    const loginForm = await superValidate(request, zod(loginSchema));
    if (!loginForm.valid) return fail(400, { loginForm });

    const urlParams = new URLSearchParams();
    urlParams.append("username", loginForm.data.mail);
    urlParams.append("password", loginForm.data.password);

    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: urlParams,
    };

    const response = await fetch(`http://nginx/api/auth/login`, requestOptions);

    if (response.status == 200) {
      const data = await response.json();
      cookies.set(
        "access_token",
        decodeURIComponent(`Bearer ${data.access_token}`),
        { path: "/" },
      );
      cookies.set(
        "refresh_token",
        decodeURIComponent(`Bearer ${data.refresh_token}`),
        {
          path: "/",
        },
      );
      throw redirect(302, "/");
    } else {
      return setError(loginForm, "Invalid email or password");
    }
  },
} satisfies Actions;
