namespace PiSync.History
{
    partial class HistoryForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panel1 = new Panel();
            btnRefreshHistory = new Button();
            label2 = new Label();
            tbSearch = new TextBox();
            lblTitle = new Label();
            panel2 = new Panel();
            lblEmpty = new Label();
            dataGridViewHistory = new DataGridView();
            panel1.SuspendLayout();
            panel2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)dataGridViewHistory).BeginInit();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.BackColor = Color.MediumPurple;
            panel1.Controls.Add(btnRefreshHistory);
            panel1.Controls.Add(label2);
            panel1.Controls.Add(tbSearch);
            panel1.Controls.Add(lblTitle);
            panel1.Dock = DockStyle.Top;
            panel1.Location = new Point(0, 0);
            panel1.Name = "panel1";
            panel1.Size = new Size(875, 79);
            panel1.TabIndex = 0;
            // 
            // btnRefreshHistory
            // 
            btnRefreshHistory.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            btnRefreshHistory.BackColor = Color.Lavender;
            btnRefreshHistory.FlatAppearance.BorderSize = 0;
            btnRefreshHistory.FlatStyle = FlatStyle.Flat;
            btnRefreshHistory.Location = new Point(729, 24);
            btnRefreshHistory.Name = "btnRefreshHistory";
            btnRefreshHistory.Size = new Size(121, 43);
            btnRefreshHistory.TabIndex = 10;
            btnRefreshHistory.Text = "REFRESH";
            btnRefreshHistory.UseVisualStyleBackColor = false;
            // 
            // label2
            // 
            label2.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            label2.AutoSize = true;
            label2.Font = new Font("Courier New", 10F);
            label2.ForeColor = Color.Lavender;
            label2.Location = new Point(490, 9);
            label2.Name = "label2";
            label2.Size = new Size(109, 20);
            label2.TabIndex = 9;
            label2.Text = "ROOM NAME:";
            // 
            // tbSearch
            // 
            tbSearch.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            tbSearch.BackColor = Color.Lavender;
            tbSearch.Location = new Point(490, 32);
            tbSearch.Name = "tbSearch";
            tbSearch.PlaceholderText = "A14";
            tbSearch.Size = new Size(225, 30);
            tbSearch.TabIndex = 8;
            // 
            // lblTitle
            // 
            lblTitle.AutoSize = true;
            lblTitle.Font = new Font("Courier New", 16F);
            lblTitle.ForeColor = Color.Lavender;
            lblTitle.Location = new Point(59, 24);
            lblTitle.Margin = new Padding(5, 0, 5, 0);
            lblTitle.Name = "lblTitle";
            lblTitle.Size = new Size(125, 30);
            lblTitle.TabIndex = 1;
            lblTitle.Text = "HISTORY";
            // 
            // panel2
            // 
            panel2.BackColor = Color.Lavender;
            panel2.Controls.Add(lblEmpty);
            panel2.Controls.Add(dataGridViewHistory);
            panel2.Dock = DockStyle.Fill;
            panel2.Location = new Point(0, 79);
            panel2.Name = "panel2";
            panel2.Size = new Size(875, 441);
            panel2.TabIndex = 1;
            // 
            // lblEmpty
            // 
            lblEmpty.AutoSize = true;
            lblEmpty.BackColor = Color.Lavender;
            lblEmpty.Font = new Font("Courier New", 16F);
            lblEmpty.ForeColor = Color.MediumPurple;
            lblEmpty.Location = new Point(327, 205);
            lblEmpty.Margin = new Padding(5, 0, 5, 0);
            lblEmpty.Name = "lblEmpty";
            lblEmpty.Size = new Size(253, 30);
            lblEmpty.TabIndex = 4;
            lblEmpty.Text = "NO HISTORY YET.";
            // 
            // dataGridViewHistory
            // 
            dataGridViewHistory.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            dataGridViewHistory.BackgroundColor = Color.Lavender;
            dataGridViewHistory.BorderStyle = BorderStyle.None;
            dataGridViewHistory.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridViewHistory.Location = new Point(19, 20);
            dataGridViewHistory.Margin = new Padding(10);
            dataGridViewHistory.Name = "dataGridViewHistory";
            dataGridViewHistory.RowHeadersWidth = 51;
            dataGridViewHistory.Size = new Size(844, 402);
            dataGridViewHistory.TabIndex = 0;
            // 
            // HistoryForm
            // 
            AutoScaleDimensions = new SizeF(12F, 22F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(875, 520);
            Controls.Add(panel2);
            Controls.Add(panel1);
            Font = new Font("Courier New", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.None;
            Margin = new Padding(4, 3, 4, 3);
            Name = "HistoryForm";
            StartPosition = FormStartPosition.Manual;
            Text = "HistoryForm";
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            panel2.ResumeLayout(false);
            panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)dataGridViewHistory).EndInit();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel1;
        private Label lblTitle;
        private Label label2;
        private TextBox tbSearch;
        private Button btnRefreshHistory;
        private Panel panel2;
        private DataGridView dataGridViewHistory;
        private Label lblEmpty;
    }
}