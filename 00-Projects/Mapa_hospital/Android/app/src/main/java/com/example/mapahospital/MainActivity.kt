package com.example.mapahospital

import android.app.DownloadManager
import android.content.Context
import android.content.Intent
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Environment
import android.view.View
import android.webkit.CookieManager
import android.webkit.URLUtil
import android.webkit.WebChromeClient
import android.webkit.WebResourceError
import android.webkit.WebResourceRequest
import android.webkit.WebStorage
import android.webkit.WebView
import android.webkit.WebViewClient
import android.widget.Toast
import androidx.appcompat.app.AlertDialog

class MainActivity : AppCompatActivity() {
    lateinit var myWebView: WebView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        myWebView = findViewById(R.id.webView)
        clearWebViewCache(myWebView)
        myWebView.webChromeClient = WebChromeClient()

        val webSettings = myWebView.settings
        webSettings.javaScriptEnabled = true
        webSettings.loadWithOverviewMode = true
        webSettings.useWideViewPort = true
        webSettings.setSupportZoom(true)
        webSettings.builtInZoomControls = true
        webSettings.displayZoomControls = false

        myWebView.webViewClient = object : WebViewClient() {
            var loadingPageShown = false

            override fun onPageFinished(view: WebView?, url: String?) {
                super.onPageFinished(view, url)
                if (!loadingPageShown) {
                    loadingPageShown = true
                    // Una vez que se haya cargado la página de espera, carga la URL principal
                    myWebView.loadUrl("https://mapahospital.ovh")
                }
            }

            override fun shouldOverrideUrlLoading(view: WebView?, request: WebResourceRequest?): Boolean {
                val url = request?.url.toString()
                if (URLUtil.isNetworkUrl(url)) {
                    val intent = Intent(Intent.ACTION_VIEW, Uri.parse(url))
                    startActivity(intent)
                    return true
                }
                return false
            }

            override fun onReceivedError(
                view: WebView,
                request: WebResourceRequest,
                error: WebResourceError
            ) {
                super.onReceivedError(view, request, error)
                // Carga una página de error personalizada
                myWebView.loadUrl("file:///android_asset/error.html")
            }
        }

        // Cargar la página de espera
        myWebView.loadUrl("file:///android_asset/waiting.html")
    }

    override fun onBackPressed() {
        AlertDialog.Builder(this)
            //.setMessage("Si quieres ir un paso atrás en la aplicación hay un botón azul con el texto 'Volver Atrás' ¿Deseas salir de la aplicación?")
            //.setCancelable(false)
            //.setPositiveButton("Sí") { _, _ -> super.onBackPressed() }
            //.setNegativeButton("No", null)
            //.show()
            myWebView.evaluateJavascript("javascript:mostrar_ventana(0)", null)
    }

    private fun clearWebViewCache(webView: WebView) {
        // Limpia el caché de la WebView
        webView.clearCache(true)

        // Limpia los datos de formularios
        webView.clearFormData()

        // Limpia el historial
        webView.clearHistory()

        // Limpia las cookies
        val cookieManager = CookieManager.getInstance()
        cookieManager.removeAllCookies(null)
        cookieManager.flush()

        // Limpia el almacenamiento local
        WebStorage.getInstance().deleteAllData()
    }

    private fun showLoadingPage() {
        // Mostrar la página de espera
        myWebView.loadUrl("file:///android_asset/waiting.html")
        myWebView.visibility = View.INVISIBLE
    }

    private fun hideLoadingPage() {
        // Ocultar la página de espera y mostrar el WebView
        myWebView.visibility = View.VISIBLE
    }
}