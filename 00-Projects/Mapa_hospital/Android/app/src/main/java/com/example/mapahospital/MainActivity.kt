package com.example.mapahospital

import android.app.DownloadManager
import android.content.Context
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Environment
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
        myWebView.loadUrl("https://mapahospital.ovh")
        myWebView.webChromeClient = WebChromeClient()

        val webSettings = myWebView.settings
        webSettings.javaScriptEnabled = true
        webSettings.loadWithOverviewMode = true
        webSettings.useWideViewPort = true
        webSettings.setSupportZoom(true)
        webSettings.builtInZoomControls = true
        webSettings.displayZoomControls = false

        myWebView.webViewClient = object : WebViewClient() {
            override fun onReceivedError(view: WebView, request: WebResourceRequest, error: WebResourceError) {
                super.onReceivedError(view, request, error)
                // Carga una página de error personalizada
                myWebView.loadUrl("file:///android_asset/error.html")
            }
            //override fun onPageFinished(view: WebView, url: String) {
            //    myWebView.evaluateJavascript("javascript:descarga_android()", null)
            //}
            override fun onPageFinished(view: WebView?, url: String?) {
                super.onPageFinished(view, url)
                // Llama a la función JavaScript después de que la página se haya cargado completamente
                view?.evaluateJavascript("javascript:descarga_android()", null)
            }
        }
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
}

